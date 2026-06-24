"""
Admin configuration for Course Platform.
Register models with admin interface for easy management.
"""
from django.contrib import admin
from .models import User, Course, Lesson, Class


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['names', 'last_names', 'email']
    search_fields = ['names', 'last_names', 'email']
    list_filter = ['names']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'get_users_count', 'get_lessons_count']
    search_fields = ['title', 'description']
    list_filter = ['title']
    filter_horizontal = ['users']

    def get_users_count(self, obj):
        return obj.users.count()
    get_users_count.short_description = 'Enrolled Users'

    def get_lessons_count(self, obj):
        return obj.lessons.count()
    get_lessons_count.short_description = 'Lessons'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order', 'get_classes_count']
    search_fields = ['title', 'course__title']
    list_filter = ['course', 'order']

    def get_classes_count(self, obj):
        return obj.classes.count()
    get_classes_count.short_description = 'Classes'


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['title', 'lesson', 'order', 'content']
    search_fields = ['title', 'lesson__title']
    list_filter = ['lesson', 'order']
