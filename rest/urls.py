from django.urls import path, include 
from rest_framework import routers
from django.urls.conf import re_path

from .views import *


router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet)
router.register(r'tweets', TweetsViewSet)
print(router.urls)

urlpatterns = [
    path('drf-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
#     # path('profile/', ProfileViewSet.as_view({'get': 'list'})),
#     # path('tweets/', TweetsViewSet.as_view({'get': 'list'})),
#     # path('tweets/<int:pk>/', TweetsViewSet.as_view({'put': 'update'})),
#     # path('tweets/delete/<int:pk>/', TweetsViewSet.as_view({'delete': 'destroy'})),
]