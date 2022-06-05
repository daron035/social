# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.utils.safestring import mark_safe
# from django.contrib.auth.models import Group

# from .models import *
# from user.forms import *

# @admin.register(User)
# class UserAdmin(UserAdmin):
    
#     list_display = ("username", "email", "first_name", "last_name", "is_staff", "get_img",)
#     readonly_fields = ("get_img",)

#     def get_img(self, obj):
#         return mark_safe(f'<img src={ obj.image.url } width="50" >')

#     get_img.short_description = 'image'


# admin.site.unregister(Group)