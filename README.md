# Quote Management System
Django app secured with JWT Authentication.

## Project Structure
```
quote_management_system/
├── db.sqlite3
├── erd.png
├── manage.py
├── readme.md
├── requirements.txt
├── quote_management_system/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── qms/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── custom_jwt_auth.py
    ├── migrations/
    │   └── __init__.py
    ├── models.py
    ├── permissions.py
    ├── serializers.py
    ├── tests/
    │   ├── __init__.py
    │   ├── test_urls.py
    │   └── test_views.py
    ├── urls.py
    └── views.py
```

## Setup Instructions
1. Make sure that python is installed (preferably 3.12).
2. Create a virtual environment using python.
3. Activate the virtual env.
4. Now, install the required dependencies listed in requirements file using the command `pip install -r requirements.txt` (Assuming the current path is same as the path where requirements.txt is located).
5. Apply the migrations with the command `python manage.py migrate` (if db.sqlite3 is absent).
6. If db.sqlite3 is absent, then run the command `python manage.py createsuperuser` to access admin at `/admin` .
7. If db.sqlite3 is present, then `username : nihal`, `password : qwerty`.
8. Now, run the command `python manage.py runserver` to run the backend server.


## How to use:
1. First create user with **Create User API**.
2. With the same credentials, obtain tokens with **Token Obtain Pair API**.
3. In **Create Quote API, Update Quote API** and **Delete Quote API**, access_token needs to sent as `Authorization : Bearer <access>`.
4. The remaining apis are open (can be accessed without token).


## API Instructions
1. **Create User API**
   - Endpoint: `/api/qms/create_user/`
   - HTTP Method: `POST`
   - Description: Creates a new user/author in the system.
   ```json
   Sample Payload:
   {
    "username": "my_boy2",
    "password": "password123",
    "email": "new_user@example.com",
    "author": {
        "pen_name": "auth_new",
        "date_of_birth": "1990-01-01"
      }
   }

    Sample Response:
    {
    "username": "my_boy2",
    "email": "new_user@example.com",
    "author": {
        "pen_name": "auth_new",
        "date_of_birth": "1990-01-01"
        }
    }

2. **List Quotes API**
   - Endpoint: `/api/qms/`
   - HTTP Method: `GET`
   - Description: Retrieves a list of all quotes in the system.
   ```json
   Sample Response:
   [
      {
        "id": 7,
        "text": "quote for uuuummy quote one by my_boy.",
        "author": {
            "pen_name": "auth_old",
            "date_of_birth": "1990-01-01"
         },
        "source": "Optional source of the quote",
        "creation_date": "2024-05-08T16:19:11.378436+05:30"
      }
   ]

3. **Create Quote API**
   - Endpoint: `/api/qms/create/`
   - HTTP Method: `POST`
   - Description: Creates a new quote in the system.
   ```json
   Sample Payload:
   {
    "text":"bid bad day",
    "source":"unknown"
   }

   Sample Response:
   {
    "id": 8,
    "text": "bid bad day",
    "author": {
        "pen_name": "auth_new",
        "date_of_birth": "1990-01-01"
      },
    "source": "unknown",
    "creation_date": "2024-05-08T18:16:38.220403+05:30"
   }

4. **Retrieve Quote API**
   - Endpoint: `/api/qms/<int:pk>/`
   - HTTP Method: `GET`
   - Description: Retrieves a specific quote by its primary key (`pk`).
   ```json
   Sample Response:
   {
    "id": 8,
    "text": "bid bad day",
    "author": {
        "pen_name": "auth_new",
        "date_of_birth": "1990-01-01"
      },
    "source": "unknown",
    "creation_date": "2024-05-08T18:16:38.220403+05:30"
   }

5. **Update Quote API**
   - Endpoint: `/api/qms/<int:pk>/update/`
   - HTTP Method: `PATCH`
   - Description: Updates an existing quote by its primary key (`pk`).
   ```json
   Sample Payload:
   {
    "text":"new day",
    "source":"NihalD"
   }

   Sample Response:
   {
    "id": 8,
    "text": "new day",
    "author": {
        "pen_name": "auth_new",
        "date_of_birth": "1990-01-01"
      },
    "source": "NihalD",
    "creation_date": "2024-05-08T18:16:38.220403+05:30"
   }

6. **Delete Quote API**
   - Endpoint: `/api/qms/<int:pk>/delete/`
   - HTTP Method: `DELETE`
   - Description: Deletes an existing quote by its primary key (`pk`).
   ```json
   Sample Response: 
      Status: 204 No Content

7. **Token Obtain Pair API**
   - Endpoint: `/api/token/`
   - HTTP Method: `POST`
   - Description: Obtains a new access and refresh token pair for authentication.
   ```json
   Sample Payload:
   {
    "username": "my_boy2",
    "password": "password123"
   }

   Sample Response:
   {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNTc3NzYyMywiaWF0IjoxNzE1MTcyODIzLCJqdGkiOiJhM2NiOWU0MTUzYjY0MDg1ODk4NGRjYTY0MTdkNzQ1NiIsInVzZXJfaWQiOjZ9.ldMg5opgFR3x-OO_vnqyyocQl70APwLdCCEwKRLqkzs",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1MTczMTIzLCJpYXQiOjE3MTUxNzI4MjMsImp0aSI6IjljM2NlNTRkMmYzYTRjNGZhZWY5ZDE5ZmY3M2NlYmQwIiwidXNlcl9pZCI6Nn0.qOM_WLHc14KvRQ_ZSo3smdBHtOUdnaN5CTxia4O1P2Q"
   }

8. **Token Refresh API**
   - Endpoint: `/api/token/refresh/`
   - HTTP Method: `POST`
   - Description: Refreshes an existing access token using a valid refresh token.
   ```json
   Sample Payload:
   {
    "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNTc3NzYyMywiaWF0IjoxNzE1MTcyODIzLCJqdGkiOiJhM2NiOWU0MTUzYjY0MDg1ODk4NGRjYTY0MTdkNzQ1NiIsInVzZXJfaWQiOjZ9.ldMg5opgFR3x-OO_vnqyyocQl70APwLdCCEwKRLqkzs"
   }

   Sample Response:
   {
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1MTczODgxLCJpYXQiOjE3MTUxNzI4MjMsImp0aSI6IjY4NWUwYjc2OGY1NzRmMzM5MDA2MzRiMTQ1ZDE2ZDY4IiwidXNlcl9pZCI6Nn0.09AncVL0OEvRrRYPz8s94xc-OxIBq8rx6Y8sbXZbbNs"
   }

## E-R Diagram
![ ``
   !\[screenshot\](erd.png)](erd.png)