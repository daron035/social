from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.forms import AuthenticationForm
from django.urls.base import reverse_lazy
from django.views.generic import View, CreateView

from .forms import *


class LoginUser(LoginView):
    template_name = 'user/login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request) 
    return redirect('public_profile_list')   


class RegisterUser(CreateView):
    template_name = 'user/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login_user')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class PasswordChangeUser(PasswordChangeView):
    template_name = 'user/change_password.html'
    success_url = reverse_lazy("password_change_done")


class PasswordChangeDoneUser(PasswordChangeDoneView):
    template_name = "user/password_change_done.html"