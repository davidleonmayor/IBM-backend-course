"""
Admin configuration for lessons app.
"""
from django.contrib import admin
from .models import Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order']
    search_fields = ['title', 'course__title']
    list_filter = ['course', 'order']
