# accounts/urls.py
from django.urls import path
from .views import login_view, logout_view, register_view, profile_view


app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    
    path('users/<str:username>/', profile_view, name='user_profile'),
    
]

