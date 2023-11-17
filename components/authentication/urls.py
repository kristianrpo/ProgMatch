"""
URL configuration for the authentication application.

This module defines the URL paths for the views related to user authentication in the application.
authentication views in the application. It includes paths for registration, login, logout, logout and other authentication related options.
and other authentication related options.

"""
from django.urls import path
from domain.useCases.authentication.signUpOptions import signUpOptions
from domain.useCases.authentication.signUpInstitution import signUpInsitution
from domain.useCases.authentication.logout import logoutFunction
from domain.useCases.authentication.login import loginFunction
from domain.useCases.authentication.signUpStudent import signUpStudent

app_name = "authApp"

urlpatterns = [
    path('signUp/', signUpOptions.as_view(), name = 'signUpOptions'),
    path('signUpInstitution/', signUpInsitution.as_view(),name = 'signUpInstitution'),
    path('signUpStudent/', signUpStudent.as_view(),name = 'signUpStudent'),
    path('logout/', logoutFunction, name = "logout"),
    path('login/',loginFunction, name = "login"),
]
