"""
URL configuration for lessons app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path("courses/<int:course_id>/lessons/", views.LessonListView.as_view(), name="lessons_list"),
    path("courses/<int:course_id>/lessons/create/", views.LessonCreateView.as_view(), name="lessons_create"),
    path("lessons/<int:pk>/", views.LessonDetailView.as_view(), name="lessons_detail"),
    path("lessons/<int:pk>/update/", views.LessonUpdateView.as_view(), name="lessons_update"),
    path("lessons/<int:pk>/delete/", views.LessonDeleteView.as_view(), name="lessons_delete"),
]
