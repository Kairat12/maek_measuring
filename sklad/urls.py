from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import *

app_name = 'sklad'

urlpatterns = [
    path('', index, name='index'),
]
