import time
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class TestUserAndEmployeeAPIs(APITestCase):

    def setUp(self):
        # Generate a unique email for each test run
        self.user_data = {
            'email': f'testuser_{int(time.time())}@example.com',  # Unique email
            'name': 'Test User',
            'password': 'testpass',
        }
        self.register_url = reverse('register')
        self.login_url = reverse('login')

        # Register the user
        registration_response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(registration_response.status_code, status.HTTP_201_CREATED)

        # Log in the user
        login_response = self.client.post(self.login_url, {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        }, format='json')

        self.token = login_response.data.get('token', {}).get('access')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        self.employee_data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'phone_number': '1234567890',
            'custom_fields': {},
        }

    def test_register(self):
        # Create another unique email for this test
        new_user_data = {
            'email': f'testuser_{int(time.time())}_new@example.com',  # Unique email
            'name': 'Another Test User',
            'password': 'testpass',
        }
        response = self.client.post(self.register_url, new_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Other test methods...
    
    def test_create_employee(self):
        response = self.client.post('/employee/api/employees/', self.employee_data, format='json')
        print("Create Employee Response:", response.data)  # Debugging line
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], self.employee_data['email'])  # Check if the email matches


    def test_update_employee(self):
    # Create an employee to update
        create_response = self.client.post('/employee/api/employees/', self.employee_data, format='json')
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
        employee_id = create_response.data['id']

        # Update employee's name
        updated_data = {
            'name': 'John Smith',
        }
        update_response = self.client.patch(f'/employee/api/employees/{employee_id}/', updated_data, format='json')
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.assertEqual(update_response.data['name'], updated_data['name'])

        # Test updating with invalid data
        invalid_update_data = {
            'email': 'not-an-email',  # Invalid email
        }
        invalid_response = self.client.patch(f'/employee/api/employees/{employee_id}/', invalid_update_data, format='json')
        self.assertEqual(invalid_response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_search_employees(self):
        # Create multiple employees
        employees = [
            {'name': 'Alice Johnson', 'email': 'alice@example.com', 'phone_number': '1112223333'},
            {'name': 'Bob Smith', 'email': 'bob@example.com', 'phone_number': '4445556666'},
            {'name': 'Charlie Brown', 'email': 'charlie@example.com', 'phone_number': '7778889999'},
        ]
        for employee in employees:
            self.client.post('/employee/api/employees/', employee, format='json')

        # Search for "Alice"
        search_response = self.client.get('/employee/api/employees/?search=Alice')
        self.assertEqual(search_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(search_response.data), 1)
        self.assertEqual(search_response.data[0]['name'], 'Alice Johnson')

        # Search for "Smith"
        search_response = self.client.get('/employee/api/employees/?search=Smith')
        self.assertEqual(search_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(search_response.data), 1)
        self.assertEqual(search_response.data[0]['name'], 'Bob Smith')

        # Search for a non-existent name
        search_response = self.client.get('/employee/api/employees/?search=NonExistent')
        self.assertEqual(search_response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(search_response.data), 0)  # Should return no result