from django.urls import path

from .views import *


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile_list/', profile_list, name='profile_list'),
    path('profile/<int:pk>/', profile, name='profile'),
    path('user_follows_list/', user_follows_list, name='user_follows_list'),
]
