from django.urls import path
from domain.useCases.learningPath.requestStudent import requestStudent
from domain.useCases.learningPath.viewLearningPath import viewLearningPath
app_name = "learningPathApp"
urlpatterns = [
    path('requestStudent/', requestStudent.as_view(), name = "requestStudent"),
    path('viewLearningPath/', viewLearningPath, name = "viewLearningPath")
]