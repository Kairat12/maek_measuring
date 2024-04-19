from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from profiles.views import profile_info, index

app_name = 'profiles'

urlpatterns = [
    path('', index, name='index'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile_info, name='profiles'),
]
