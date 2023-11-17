from django.urls import path
from domain.useCases.student.viewInfoStudent import viewInfoStudent
app_name = "studentApp"
urlpatterns = [
    path('viewInfoStudent/<pk>',viewInfoStudent.as_view(), name = "viewInfoStudent"),
]