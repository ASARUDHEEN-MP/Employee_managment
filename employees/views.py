from rest_framework import viewsets
from .models import Employee,CustomField
from .serializer import EmployeeSerializer,CustomFieldSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from django.db import transaction
import logging



logger = logging.getLogger('employees.view')

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

   def get_queryset(self):
        queryset = Employee.objects.filter(user=self.request.user)
        
        # Get the 'search' query parameter
        search = self.request.query_params.get('search', None)
        if search:
            # Filter by name, email, or phone number
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(email__icontains=search) |
                Q(phone_number__icontains=search)
            )
            
        return queryset

    def create(self, request):
        try:
            request.data['user'] = request.user.id
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                logger.info('Employee created successfully: %s', serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            logger.warning('Failed to create employee: %s', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error('Error creating employee: %s', e)
            return Response({'error': 'An error occurred while creating the employee.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

    def update(self, request, *args, **kwargs):
        try:
            employee = self.get_object()
            request.data.pop('user', None)  # Remove user from the request data
            serializer = self.get_serializer(employee, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                logger.info('Employee updated successfully: %s', serializer.data)
                return Response(serializer.data)

            logger.warning('Failed to update employee: %s', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error('Error updating employee: %s', e)
            return Response({'error': 'An error occurred while updating the employee.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




    def retrieve(self, request, pk=None):
        try:
            employee = self.get_object()
            serializer = self.get_serializer(employee)
            return Response(serializer.data)
        except Exception as e:
            logger.error('Error retrieving employee: %s', e)
            return Response({'error': 'Employee not found.'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            employee = self.get_object()
            employee.delete()
            logger.info('Employee deleted successfully: %s', employee.id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logger.error('Error deleting employee: %s', e)
            return Response({'error': 'An error occurred while deleting the employee.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class CustomFieldViewSet(viewsets.ModelViewSet):
    queryset = CustomField.objects.all()
    serializer_class = CustomFieldSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CustomField.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Automatically set the user

    def perform_destroy(self, instance):
        # Get the custom field name to clean up related Employee data
        field_name = instance.field_name
        logger.info('Attempting to delete custom field: %s', field_name)
        try:
            # Start a transaction to ensure atomic updates
            with transaction.atomic():
                # Get all employees related to the user
                employees = Employee.objects.filter(user=self.request.user)

                # Iterate over each employee and update their custom_fields
                for employee in employees:
                    custom_fields = employee.custom_fields
                    if field_name in custom_fields:
                        # Remove the custom field
                        del custom_fields[field_name]
                        # Update the employee record
                        employee.custom_fields = custom_fields
                        employee.save(update_fields=['custom_fields'])
            logger.info('Custom field deleted and employees updated: %s', field_name)
            # Now call the superclass method to delete the custom field
            super().perform_destroy(instance)
        except Exception as e:
            logger.error('Error deleting custom field: %s', e)
            raise  # Re-raise the exception after logging
