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

- **URL**: `http://127.0.0.1:8000/api/employees/`
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

- **URL**: `http://127.0.0.1:8000/api/employees/{employyeid}`
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
 
- **URL**: `http://127.0.0.1:8000/api/employees/{employyeid}`
- **Method**: `DELETE`
- **Request Body**:
  ```json
 
- **Response**: 
    - On successful login:
        ```json
            {
        "deleted successfully....
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


### 5. Search Employees

**Search Employees**

- **URL**: `http://127.0.0.1:8000/api/employees/`
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
