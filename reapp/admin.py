from django.contrib import admin

# Register your models here.
# reapp/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import RepicUser

class RepicUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone_number', 'location', 'is_staff')
    search_fields = ('username', 'email', 'phone_number')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'phone_number', 'location')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(RepicUser, RepicUserAdmin)