from django.db import models
from user_account.models import CustomUser  # Directly import the CustomUser model

class Employee(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    custom_fields = models.JSONField(default=dict)

    def __str__(self):
        return self.name


class CustomField(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=100)
    field_type = models.CharField(max_length=50)  # e.g., 'text', 'number'

    def __str__(self):
        return f"{self.field_name} ({self.field_type})"