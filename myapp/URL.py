from django.contrib import admin
from django.urls import path

from myfirstapp import views
from myfirstapp.views import MyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path ('home/',views.home,name='home'),
    path('my_template/',MyView.as_view(),name='my_template'),
]
