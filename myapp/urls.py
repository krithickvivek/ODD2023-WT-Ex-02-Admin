from django.contrib import admin
from django.urls import path

from myapp import views
from myapp.views import create_users


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_users/',views.create_users,name='create_users'),
]
