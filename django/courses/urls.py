"""
URL configuration for courses app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path("courses/", views.CourseListView.as_view(), name="courses_list"),
    path("courses/create/", views.CourseCreateView.as_view(), name="courses_create"),
    path("courses/<int:pk>/", views.CourseDetailView.as_view(), name="courses_detail"),
    path("courses/<int:pk>/update/", views.CourseUpdateView.as_view(), name="courses_update"),
    path("courses/<int:pk>/delete/", views.CourseDeleteView.as_view(), name="courses_delete"),
    path("enroll/", views.EnrollView.as_view(), name="courses_enroll"),
]
