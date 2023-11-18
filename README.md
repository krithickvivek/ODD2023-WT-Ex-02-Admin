# Ex-02-Admin
NAME:Krithick Vivekananda
REF.NO:23009445

# AIM:
Create a Django website with five users. Two users are to be staff users (including admin) and the other three users are non-staff users.


# Design Procedure:

## Step 1: 
Create a Django Project by
django-admin startproject myproject
## Step 2: 
Create a Django app within your project using the following command:
cd myproject
python manage.py startapp myapp
## Step 3: 
Define User Creation View

In your app's views.py file (myapp/views.py), define a view function to create the users with the specified attributes.

To create a Django website with five users (two staff users, including an admin, and three non-staff users), set email, first name, and last name for all users, you can use the following Python view function:
```python
from django.contrib.auth.models import User
from django.views import View
from django.shortcuts import render

def create_users(request):
    admin_user=User.objects.create_user(username='admin',password='adminpass')
    admin_user.is_staff = True
    admin_user.is_superuser = True
    admin_user.email = 'admin@example.com'
    admin_user.first_name = 'Admin'
    admin_user.last_name = 'User'
    admin_user.save()

    staff_user1 = User.objects.create_user(username='staff1',password='staffipass')
    staff_user1.is_staff = True
    staff_user1.email = 'staff1@example.com'
    staff_user1.first_name ='Staff'
    staff_user1.last_name ='User1'
    staff_user1.save()

    user1 = User.objects.create_user(username='user1',password='user1pass')
    user1.email='user1@example.com'
    user1.first_name='User'
    user1.last_name='One'
    user1.save()

    user2 = User.objects.create_user(username='user2',password='user12pass')
    user2.email='user2@example.com'
    user2.first_name='User'
    user2.last_name='Two'
    user2.save()

    user3 = User.objects.create_user(username='user3',password='user3pass')
    user3.email='user3@example.com'
    user3.first_name='User'
    user3.last_name='Three'
    user3.save()

    return render(request, ' myfirstapp/user_creation_success.html')
```

## Step 4: 
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

## Step 5:
Define URL Pattern

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
## Step 6: 
Apply migrations to create the necessary database tables for the User model.
    python manage.py makemigrations
    python manage.py migrate

## Step 7:
Start the development server to run your Django application.
python manage.py runserver

## Step 8:
Access the User Creation View by
Visit http://localhost:8000/create_users/ in your web browser to execute the create_users view and create the users.

## Step 9:
You can verify that the users have been created with the specified attributes by checking the Django admin interface.


# Output:
![djangolatest](https://github.com/krithickvivek/ODD2023-WT-Ex-02-Admin/assets/139331296/a878c03b-6004-433f-872c-901329b3674a)

# Result:
The program is excecuted successfully.



