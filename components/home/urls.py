from django.urls import path
from domain.useCases.home.viewHome import viewHome
app_name = "homeApp"
urlpatterns = [
    path('', viewHome.as_view(), name = "viewHomePage")
]