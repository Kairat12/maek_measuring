from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from profiles.views import profile_info
from .views import *

app_name = 'devices'

urlpatterns = [
    path('', index, name='index'),
    path('devices/', devices_page, name='devices_page'),
]
