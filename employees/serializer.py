from rest_framework import serializers
from .models import Employee,CustomField


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'user', 'name', 'email', 'phone_number', 'custom_fields']

    def validate_custom_fields(self, value):
        # Get the user's custom fields
        user_custom_fields = CustomField.objects.filter(user=self.context['request'].user).values_list('field_name', flat=True)

        # Check for invalid fields
        invalid_fields = [key for key in value.keys() if key not in user_custom_fields]
        if invalid_fields:
            raise serializers.ValidationError(f"Invalid custom fields: {', '.join(invalid_fields)}")

        return value


class CustomFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomField
        fields = ['id', 'user', 'field_name', 'field_type']
        read_only_fields = ['user']  # Prevent user from being set manually
    

    def validate_field_name(self, value):
        user = self.context['request'].user
        if CustomField.objects.filter(user=user, field_name=value).exists():
            raise serializers.ValidationError("A custom field with this name already exists for this user.")
        return value
    
    