"""
Admin configuration for accounts app.
"""
from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['names', 'last_names', 'email']
    search_fields = ['names', 'last_names', 'email']
    list_filter = ['names']
