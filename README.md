# Employee Management System

## Overview
This project is an Employee Management System that allows users to sign up, manage employees, and dynamically handle employee fields. The system features a user-friendly interface for managing employee data and includes robust search functionality.

### Technologies Used
- **Database**: PostgreSQL for data storage.
- **Caching**: Redis for caching employee data.
- **Logging**: Integrated logging for monitoring application behavior.
- **Testing**: Django's testing framework for API testing.

### Multi-User Support
The system supports multiple users, ensuring that:
- Each user can manage their own set of employees.
- Changes made to employee fields by one user do not affect other users' data.
- Employees are listed under the corresponding user.

## Features
- **User Authentication**: Signup page for users to create an account.
- **Dashboard**: A simple dashboard for navigating the employee module.
- **Employee Module**:
  - View a list of employees with search capability.
  - Create new employee records using a modal form.
- **Dynamic Field Management**: Manage employee fields from a settings section, allowing users to add and modify fields dynamically.

## Installation

### Prerequisites
- Python 3.x
- Django
- PostgreSQL
- Redis (for caching, optional)

### Steps


### Clone the Repository and Set Up the Environment
Follow these steps to clone the repository and set up the virtual environment:

1. Clone the repository:
    ```bash
    git clone https://github.com/ASARUDHEEN-MP/Employee_managment.git
    ```

2. Navigate into the project directory:
    ```bash
    cd Employee_managment
    ```

3. Create a virtual environment:
    ```bash
    python -m venv venv


    ```

4. Activate the virtual environment:
    - For macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    - For Windows:
        ```bash
        venv\Scripts\activate
        ```

5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Create a .env File
Create a `.env` file in the project directory to store your database configuration. Use the following template:

```plaintext
# Database settings
DB_NAME='your_database_name'
DB_USER='postgres'
DB_PASSWORD='your_password'
DB_HOST='localhost'
DB_PORT=5432
```
7.Run Migrations
```bash
    python3 manage.py migrate

```
8.Start the Server
```bash
    python3 manage.py runserver
```
You can now access the API at http://127.0.0.1:8000/

9.Testing
```bash
    python manage.py test employees
```
## API Endpoints

### 1. User Registration
- **URL**: `http://127.0.0.1:8000/auth/api/register/`
- **Method**: `POST`
- **Request Body**: 
    ```json
     {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "password": "yourpassword"
  }

    ```
- **Response**: 
    - On successful registration:
        ```json
        {
            "message": "User registration is successful..."
        }
        ```
    - On error (e.g., validation errors):
        ```json
        {
            "errors": {
                "email": ["This field is required."],
                "name": ["This field is required."],
                "password": ["This field is required."]
            }
        }
        ```
### 2. User Login
- **URL**: `http://127.0.0.1:8000/auth/api/login/`
- **Method**: `POST`
- **Request Body**: 
    ```json
       {
      "email": "johndoe@example.com",
      "password": "yourpassword"
    }
    ```
- **Response**: 
    - On successful login:
        ```json
        {
        "userInfo": {
            "id": 0,
            "email": "johndoe@example.com",
            "name": "hello",
            "is_superuser": false,
            "last_login": "2024s-10-26T11:54:19.615707Z",
            "is_active": true
        },
        "token": {
            "refresh": "eyJhbGczMDAzMDA1OSwiaWF0IjoxNzI5OTQzNjU5LCJqdGkiOiJmODQ4N2M4YmFhODE0YmU4OWE1OGE2ZDNiN2E4Mjg4OSIsInVzZXJfaWQiOjh9.AQD0ZmpN6l7E1BTEs2iDcdAgKJ8rsiCI6QpXrBtzh6E",
            "access": "eyJhbGciOiJIUzI5NDM2NTksImp0aSI6IjgyN2MzOTIwZWZhMDRkZGViYzkyOTM3MDUxYWZmNTU0IiwidXNlcl9pZCI6OH0.U9r9H01iL6NyodJ0b3JSci2rqOZ9Zh2R_Yzb5jThmCY"
        },
        "message": "Successfully logged in",
        "status": 200
      }
        ```
    - On error (e.g., validation errors if password or username is null):
        ```json
        {
            "errors": {
                "name": ["This field is required."],
                "password": ["This field is required."]
            }
        }
        ```
        Or for invalid credentials:
        ```json
        {
            "errors": {
                "non_field_errors": [
                    "Invalid password."
                ]
            }
        }
        ```
        Or:
        ```json
        {
            "errors": {
                "non_field_errors": [
                    "Invalid email."
                ]
            }
        }
        ```
### 3. user Home


**Create Employee **

- **URL**: `http://127.0.0.1:8000/employee/api/employees/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone_number": "1234567890"
  }
- **Response**: 
    - On successful login:
        ```json
        {
        "id": 1,
        "user": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone_number": "1234567890",
        "custom_fields": {}
      }

        ```
    - On error (e.g., validation errors if password or username is null):
        ```json
        {
            "errors": {
                "name": ["This field is required."],
                "password": ["This field is required."]
            }
        }
        ```
        Or for invalid credentials:
        ```json
               {
        "error": "This field is required."
      }

        ```
        Or:
        ```json
        {
        "error": "An unexpected error occurred."
      }

        ```

 **update Employee **

- **URL**: `http://127.0.0.1:8000/employee/api/employees/{employyeid}`
- **Method**: `PUT`
- **Request Body**:
  ```json
  {
  "name": "John Smith",
  "email": "john.smith@example.com",
  "phone_number": "0987654321"
  }

- **Response**: 
    - On successful login:
        ```json
            {
        "id": 1,
        "user": 1,
        "name": "John Smith",
        "email": "john.smith@example.com",
        "phone_number": "0987654321",
        "custom_fields": {}
      }
      

        ```
    - On error (e.g., validation errors if password or username is null):
        ```json
        {
        "error": "This field is required."
      }

        ```
        Or for invalid credentials:
        ```json
            {
            "error": "Employee not found."
          }

        ```
        Or:
        ```json
        {
        "error": "An unexpected error occurred."
      }

        ```

 **DELETE Employee **
 
- **URL**: `http://127.0.0.1:8000/employee/api/employees/{employyeid}`
- **Method**: `DELETE`

 
- **Response**: 
  
- **204 No Content::**
  - **Description**: Description: Custom field deleted successfully. Employee records updated accordingly.
    - On error (e.g., validation errors if password or username is null):
       

        ```
        Or for invalid credentials:
        ```json
            {
            "error": "Employee not found."
          }

        ```
        Or:
        ```json
        {
        "error": "An unexpected error occurred."
      }

        ```


### 5. Search Employees

**Search Employees**

- **URL**: `http://127.0.0.1:8000/employee/api/employees/`
- **Method**: `GET`
- **Query Parameters**:
  - `search`: (optional) A string to search for in employee names, emails, or phone numbers.("http://127.0.0.1:8000/employee/api/employees/?search=manu@g")

**Responses**
- **200 OK:**
  - **Description**: Returns a list of employees matching the search criteria.
  - **Example**:
  ```json
  [
    {
      "id": 2,
      "user": 1,
      "name": "Alice Johnson",
      "email": "alice.johnson@example.com",
      "phone_number": "9876543210",
      "custom_fields": {}
    }
  ]

### 6. Dynamic fields for  Employees

**Here name,phonenumber,email is static field and able to add more fields and delete the fields also  and the fields add by a user not be effect to the other user**


#### Create Custom Field

- **URL**: `http://127.0.0.1:8000/employee/api/custom-fields/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "field_name": "Custom Field Name",
    "field_type": "text"  
  }

**Responses**
- **200 OK:**
  - **Description**: Custom field created successfully..
  - **Example**:
  ```json
       {
    "id": 1,
    "user": 1,
    "field_name": "Custom Field Name",
      "field_type": "text"
    }

- **400 OK:**
  - **Description**: Custom field created successfully..
  - **Example**:
  ```json
     {
      "error": "A custom field with this name already exists for this user."
    }



- **URL**: `http://127.0.0.1:8000/employee/api/custom-fields/{id}/`
- **Method**: `DELETE`

**Responses**
- **204 No Content::**
  - **Description**: Description: Custom field deleted successfully. Employee records updated accordingly.
 
- **400 OK:**
  - **Description**: Custom field created successfully..
  - **Example**:
  ```json
     {
      "error": "A custom field with this name already exists for this user."
    }

  
**Create Employee **

- **URL**: `http://127.0.0.1:8000/employee/api/employees/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone_number": "1234567890",
    "Custom Field Name":"value(int,str)"
  
  }
- **Response**: 
    - On successful login:
        ```json
        {
        "id": 1,
        "user": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone_number": "1234567890",
        "custom_fields": {"Custom Field Name":"value(int,str)"}
      }
  ```
- **400 Bad Request**:
  ```json
       {
        "error": "Invalid custom field: \"name of that field\""
      }
  ```
  
   -> You can test the appliaction:
    ```bash
    python manage.py test employees
    ```
     ```bash
                   

        Found 4 test(s).
        Creating test database for alias 'default'...
        System check identified no issues (0 silenced).
          INFO 2024-10-27 07:35:16,687 views Employee created successfully: {'id': 1, 'user': 1, 'name': 'John Doe', 'email': 'johndoe@example.com', 'phone_number': '1234567890', 'custom_fields': {}}
          Create Employee Response: {'id': 1, 'user': 1, 'name': 'John Doe', 'email': 'johndoe@example.com', 'phone_number': '1234567890', 'custom_fields': {}}
          ..INFO 2024-10-27 07:35:18,431 views Employee created successfully: {'id': 2, 'user': 4, 'name': 'Alice Johnson', 'email': 'alice@example.com', 'phone_number': '1112223333', 'custom_fields': {}}
          INFO 2024-10-27 07:35:18,434 views Employee created successfully: {'id': 3, 'user': 4, 'name': 'Bob Smith', 'email': 'bob@example.com', 'phone_number': '4445556666', 'custom_fields': {}}
          INFO 2024-10-27 07:35:18,437 views Employee created successfully: {'id': 4, 'user': 4, 'name': 'Charlie Brown', 'email': 'charlie@example.com', 'phone_number': '7778889999', 'custom_fields': {}}
          .INFO 2024-10-27 07:35:19,147 views Employee created successfully: {'id': 5, 'user': 5, 'name': 'John Doe', 'email': 'johndoe@example.com', 'phone_number': '1234567890', 'custom_fields': {}}
          INFO 2024-10-27 07:35:19,149 views Employee updated successfully: {'id': 5, 'user': 5, 'name': 'John Smith', 'email': 'johndoe@example.com', 'phone_number': '1234567890', 'custom_fields': {}}
          WARNING 2024-10-27 07:35:19,152 views Failed to update employee: {'email': [ErrorDetail(string='Enter a valid email address.', code='invalid')]}
          .
        ----------------------------------------------------------------------
        Ran 4 tests in 3.197s
        
        OK
        Destroying test database for alias 'default'...
        
    ```
        -> Also have a file to log the bug,info:
    ```bash
    INFO 2024-10-26 10:38:01,950 views Employee created successfully: {'id': 50, 'user': 3, 'name': 'asarudhen', 'email': 'a@1234gmail.com', 'phone_number': '132', 'custom_fields': {'experience': '21'}}
  INFO 2024-10-26 10:38:10,891 views Employee data retrieved from Redis cache.
  INFO 2024-10-26 10:38:10,901 views Employee updated successfully: {'id': 49, 'user': 3, 'name': 'asarudheen', 'email': 'a@gmail.com', 'phone_number': '793', 'custom_fields': {'experience': '122'}}
  INFO 2024-10-26 10:38:21,758 views Employee data retrieved from Redis cache.
  INFO 2024-10-26 10:38:21,774 views Employee data retrieved from Redis cache.
  INFO 2024-10-26 10:38:27,769 views Employee data retrieved from Redis cache.
  INFO 2024-10-26 10:38:27,777 views Employee updated successfully: {'id': 50, 'user': 3, 'name': 'asarudhen', 'email': 'a@1234gmail.com', 'phone_number': '132', 'custom_fields': {'experience': '21', 'age': '23'}}
  INFO 2024-10-26 11:24:18,994 views Employee data retrieved from Redis cache.
  INFO 2024-10-26 11:24:19,012 views Employee data retrieved from Redis cache.
  INFO 2024-10-26 11:41:05,432 views All employee data cached in Redis.
  INFO 2024-10-26 11:41:05,446 views Employee data retrieved from Redis cache.
  INFO 2024-10-26 18:31:51,785 views Employee created successfully: {'id': 3, 'user': 1, 'name': 'manuu won', 'email': 'manaaf@gmail.com', 'phone_number': '804', 'custom_fields': {}}
  WARNING 2024-10-26 18:34:06,677 views Failed to create employee: {'email': [ErrorDetail(string='employee with this email already exists.', code='unique')]}
  INFO 2024-10-26 18:34:16,225 views All employee data cached in Redis.
  INFO 2024-10-26 18:56:51,947 views Employee created successfully: {'id': 51, 'user': 6, 'name': 'k', 'email': 't@hmail.com', 'phone_number': '5632', 'custom_fields': {}}
  ERROR 2024-10-26 18:57:21,906 views Error retrieving employee: 
  INFO 2024-10-27 07:35:16,687 views Employee created successfully: {'id': 1, 'user': 1, 'name': 'John Doe', 'email': 'johndoe@example.com', 'phone_number': '1234567890', 'custom_fields': {}}
  INFO 2024-10-27 07:35:18,431 views Employee created successfully: {'id': 2, 'user': 4, 'name': 'Alice Johnson', 'email': 'alice@example.com', 'phone_number': '1112223333', 'custom_fields': {}}
  INFO 2024-10-27 07:35:18,434 views Employee created successfully: {'id': 3, 'user': 4, 'name': 'Bob Smith', 'email': 'bob@example.com', 'phone_number': '4445556666', 'custom_fields': {}}
  INFO 2024-10-27 07:35:18,437 views Employee created successfully: {'id': 4, 'user': 4, 'name': 'Charlie Brown', 'email': 'charlie@example.com', 'phone_number': '7778889999', 'custom_fields': {}}
  INFO 2024-10-27 07:35:19,147 views Employee created successfully: {'id': 5, 'user': 5, 'name': 'John Doe', 'email': 'johndoe@example.com', 'phone_number': '1234567890', 'custom_fields': {}}
  INFO 2024-10-27 07:35:19,149 views Employee updated successfully: {'id': 5, 'user': 5, 'name': 'John Smith', 'email': 'johndoe@example.com', 'phone_number': '1234567890', 'custom_fields': {}}
  WARNING 2024-10-27 07:35:19,152 views Failed to update employee: {'email': [ErrorDetail(string='Enter a valid email address.', code='invalid')]}
  
      ```
