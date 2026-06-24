"""
URL configuration for classes app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path("lessons/<int:lesson_id>/classes/", views.ClassroomListView.as_view(), name="classroom_list"),
    path("lessons/<int:lesson_id>/classes/create/", views.ClassroomCreateView.as_view(), name="classroom_create"),
    path("classes/<int:pk>/", views.ClassroomDetailView.as_view(), name="classroom_detail"),
    path("classes/<int:pk>/update/", views.ClassroomUpdateView.as_view(), name="classroom_update"),
    path("classes/<int:pk>/delete/", views.ClassroomDeleteView.as_view(), name="classroom_delete"),
]
