# Ex-02-Admin User using function-based views
NAME:Krithick Vivekananda
REF.NO:23009445

# AIM:
Create a Django website with five users. Two users are to be staff users (including admin) and the other three users are non-staff users.
1. Creating five users

2. Two staff users and three non-staff users

3. Setting e-mail for all users

4. Setting the first name and last name for all users.

# Design Procedure:

## Step 1: Create a Django Projet
Create a Django Project 
django-admin startproject myproject
## Step 2: Create a Django App
Create a Django app within your project using the following command:
cd myproject
python manage.py startapp myapp
## Step 3: Define User Creation View
In your app's views.py file (myapp/views.py), define a view function to create the users with the specified attributes.

## Step 4: Create Templates
Create a template directory within your app (myapp/templates) if it doesn't already exist. Inside this directory, create a template named 'user_creation_success.html' to display a success message.
```html
<html>
    <body>
        <h1>
            Successfully Created
        </h1>
    </body>
</html>
```

## Step 5:Define URL Pattern
In your app's urls.py file (myapp/urls.py), define a URL pattern to route to the create_users view.
```python
from django.contrib import admin
from django.urls import path

from myapp import views
from myapp.views import create_users


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_users/',views.create_users,name='create_users'),
]

```
## Step 6: Apply Migrations
Apply migrations to create the necessary database tables for the User model.
    python manage.py makemigrations
    python manage.py migrate

## Step 7: Run the Development Server
Start the development server to run your Django application.
python manage.py runserver

## Step 8: Access the User Creation View
Access the User Creation View by
Visit http://localhost:8000/create_users/ in your web browser to execute the create_users view and create the users.

## Step 9: Veriy the Users
You can verify that the users have been created with the specified attributes by checking the Django admin interface.


# Output:
![djangolatest](https://github.com/krithickvivek/ODD2023-WT-Ex-02-Admin/assets/139331296/a878c03b-6004-433f-872c-901329b3674a)

# Result:
The program is excecuted successfully.



