from django.urls import path
from domain.useCases.student.viewInfoStudent import viewInfoStudent
from domain.useCases.student.updateInfoStudent import updateInfoStudent
from domain.useCases.student.deleteStudent import deleteStudent
from domain.useCases.student.viewHomeStudent import viewHomeStudent
app_name = "studentApp"
urlpatterns = [
    path('viewInfoStudent/<pk>',viewInfoStudent.as_view(), name = "viewInfoStudent"),
    path('updateInfoStudent/<pk>',updateInfoStudent.as_view(), name = "updateInfoStudent"),
    path('deleteStudent/<pk>',deleteStudent.as_view(), name = "deleteStudent"),
    path('viewHomeStudent/', viewHomeStudent.as_view(),name = "viewHomeStudent")
]