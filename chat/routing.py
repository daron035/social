from django.urls import re_path, path

from .consumers import *

websocket_urlpatterns = [
    re_path(r'ws/chat/room/(?P<room_id>\d+)/$', ChatConsumer.as_asgi()),
]