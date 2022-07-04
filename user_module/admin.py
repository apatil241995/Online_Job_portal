from django.contrib import admin
from .models import CustomUsers
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.


class UserModelAdmin(BaseUserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email',
                    'full_name',
                    'is_active',
                    'role'
                    )
    list_filter = ('email', 'is_active', )
    fieldsets = (
        ('User_Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('role', 'is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name',
                       'role', 'password1', 'password2', 'is_active'),
        }),
    )
    search_fields = ('email',)
    ordering = ('id',)
    filter_horizontal = ()


# Registering the new UserAdmin...
admin.site.register(CustomUsers, UserModelAdmin)
