"""
URL configuration for accounts app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="accounts_signup"),
    path("login/", views.LoginView.as_view(), name="accounts_login"),
]
