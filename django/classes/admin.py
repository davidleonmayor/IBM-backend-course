"""
Admin configuration for classes app.
"""
from django.contrib import admin
from .models import Classroom


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['title', 'lesson', 'order', 'duration']
    search_fields = ['title', 'lesson__title']
    list_filter = ['lesson', 'order']
