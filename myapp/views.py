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