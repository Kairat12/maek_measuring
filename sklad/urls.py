from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import *

app_name = 'sklad'

urlpatterns = [
    path('', index, name='index'),
    path('main_sklad/', main_sklad, name='main_sklad'),
    path('main_sklad/report', main_sklad_report, name='main_sklad_report'),
]
