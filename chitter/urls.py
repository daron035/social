from django.urls import path
from django.conf.urls.static import static

from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('profile_list/', profile_list, name='profile_list'),
    path('public_profile_list/', public_profile_list, name='public_profile_list'), # for user unregistere
    path('profile/<int:pk>/', profile, name='profile'),
    path('user_follows_list/', user_follows_list, name='user_follows_list'),

    path('user_friends_list/', user_friends_list, name='user_friends_list'),
    path('all_users_list/', UserList.as_view(), name='all_users_list'),
    path('add_friend/<int:pk>/', accept_friend_request, name='add_friend'),
    path('decline_friend_request/<int:pk>/', decline_friend_request, name='decline_friend_request'),
    path('send_friend_request/<int:pk>/', send_friend_request, name='send_friend_request'),
]