from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import *

app_name = 'contract_status'

urlpatterns = [
    path('contract_status', contract_status, name='contract_status'),
]
