from django.urls import path
from domain.useCases.learningPath.requestStudent import requestStudent
app_name = "learningPathApp"
urlpatterns = [
    path('requestStudent/', requestStudent.as_view(), name = "requestStudent"),
]