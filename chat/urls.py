from django.urls import path
from django.urls import re_path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('room/<int:room_id>/', room, name='room'),
    path('<int:pk>/', create_or_return_private_chat, name='create_room'),
]