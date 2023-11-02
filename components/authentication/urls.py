from django.urls import path
from domain.useCases.authentication.signUpOptions import signUpOptions
app_name = "authApp"

urlpatterns = [
    path('signUp/', signUpOptions.as_view(), name = 'signUpOptions')
]
