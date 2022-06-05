from django.conf import settings
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Login", widget=forms.TextInput())
    email = forms.EmailField(label="Email", widget=forms.EmailInput())
    image = forms.ImageField(label="Image")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False

# """ Change UserCreationForm in Django Admin (added email input field """
# class UserCreateForm(UserCreationForm):
    
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'first_name' , 'last_name', )


# class UserAdmin(UserAdmin):
#     add_form = UserCreateForm
#     # prepopulated_fields = {'username': ('first_name' , 'last_name', )}

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'email', 'password1', 'password2', ),
#         }),
#     )