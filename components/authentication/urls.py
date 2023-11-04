from django.urls import path
from domain.useCases.authentication.signUpOptions import signUpOptions
from domain.useCases.authentication.signUpInstitution import singUpInsitution
app_name = "authApp"

urlpatterns = [
    path('signUp/', signUpOptions.as_view(), name = 'signUpOptions'),
    path('signUpInstitution/', singUpInsitution.as_view(),name = 'signUpInstitution')
]
