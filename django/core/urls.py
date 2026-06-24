"""
URL configuration for core app.
Class-based views for Course Platform.
"""
from django.urls import path
from . import views

urlpatterns = [
    # ============================================
    # AUTH VIEWS
    # ============================================
    path("signup/", views.SignupView.as_view(), name="core_signup"),
    path("login/", views.LoginView.as_view(), name="core_login"),
    
    # ============================================
    # COURSE VIEWS
    # ============================================
    path("courses/", views.CourseListView.as_view(), name="core_course_list"),
    path("courses/create/", views.CourseCreateView.as_view(), name="core_course_create"),
    path("courses/<int:pk>/", views.CourseDetailView.as_view(), name="core_course_detail"),
    path("courses/<int:pk>/update/", views.CourseUpdateView.as_view(), name="core_course_update"),
    path("courses/<int:pk>/delete/", views.CourseDeleteView.as_view(), name="core_course_delete"),
    
    # ============================================
    # LESSON VIEWS
    # ============================================
    path("courses/<int:course_id>/lessons/", views.LessonListView.as_view(), name="core_lesson_list"),
    path("courses/<int:course_id>/lessons/create/", views.LessonCreateView.as_view(), name="core_lesson_create"),
    path("lessons/<int:pk>/", views.LessonDetailView.as_view(), name="core_lesson_detail"),
    path("lessons/<int:pk>/update/", views.LessonUpdateView.as_view(), name="core_lesson_update"),
    path("lessons/<int:pk>/delete/", views.LessonDeleteView.as_view(), name="core_lesson_delete"),
    
    # ============================================
    # CLASS VIEWS
    # ============================================
    path("lessons/<int:lesson_id>/classes/", views.ClassListView.as_view(), name="core_class_list"),
    path("lessons/<int:lesson_id>/classes/create/", views.ClassCreateView.as_view(), name="core_class_create"),
    path("classes/<int:pk>/", views.ClassDetailView.as_view(), name="core_class_detail"),
    path("classes/<int:pk>/update/", views.ClassUpdateView.as_view(), name="core_class_update"),
    path("classes/<int:pk>/delete/", views.ClassDeleteView.as_view(), name="core_class_delete"),
    
    # ============================================
    # ENROLLMENT VIEW
    # ============================================
    path("enroll/", views.EnrollView.as_view(), name="core_enroll"),
]
