from django.urls import path, include
from django.views.generic import TemplateView

from .views import *


urlpatterns = [
    path('login/', LoginUser.as_view(), name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('register/', RegisterUser.as_view(), name='register_user'),

    path(
        "password_change/", PasswordChangeUser.as_view(), name="password_change"
    ),
    path(
        "password_change/done/", PasswordChangeDoneUser.as_view(), name="password_change_done",
    ),

    # path('', include('django.contrib.auth.urls')),
]