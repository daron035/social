from django.urls import path

from .views import *


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile_list/', profile_list, name='profile_list'),
    path('profile/<int:pk>/', profile, name='profile'),
    path('user_follows_list/', user_follows_list, name='user_follows_list'),

    path('user_friends_list/', user_friends_list, name='user_friends_list'),
    path('add_friend/<int:pk>/', accept_friend_request, name='add_friend'),
    path('decline_friend_request/<int:pk>/', decline_friend_request, name='decline_friend_request'),
    path('send_friend_request/<int:pk>/', send_friend_request, name='send_friend_request'),
]
