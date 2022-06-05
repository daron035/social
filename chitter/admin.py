from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from django.contrib.auth.models import Group

from django.contrib.auth.forms import UserCreationForm

from .models import *
from user.models import *

from user.forms import *


""" Change UserCreationForm in Django Admin (added email input field) """
class UserCreateForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name' , 'last_name', )


class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 0


@admin.register(User)
class UserAdmin(UserAdmin):
    
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "get_img",)
    readonly_fields = ("get_img",)
    inlines = [ProfileInline]

    add_fieldsets = ( # django admin add email field 
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', ),
        }),
    )

    def get_inline_instances(self, request, obj=None): # Hide Inline form in Django
        return obj and super(UserAdmin, self).get_inline_instances(request, obj) or []

    def get_img(self, obj):
        return mark_safe(f'<img src={ obj.image.url } width="50" >')

    get_img.short_description = 'image'



@admin.register(Tweets)
class TweetsAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'time_admin')



admin.site.register(Profile)
admin.site.unregister(Group)