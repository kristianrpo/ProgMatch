from django.urls import path
from .views import ModelView
app_name = "institutionApp"
urlpatterns = [
    path('',ModelView.as_view())
]