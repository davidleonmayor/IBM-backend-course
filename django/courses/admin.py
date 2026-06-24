"""
Admin configuration for courses app.
"""
from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'get_users_count']
    search_fields = ['title', 'description']
    list_filter = ['title']
    filter_horizontal = ['users']

    def get_users_count(self, obj):
        return obj.users.count()
    get_users_count.short_description = 'Enrolled Users'
