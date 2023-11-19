from django.urls import path
from domain.useCases.course.addCourses import populate_database
app_name = "courseApp"
urlpatterns = [
    path('populate-database/', populate_database, name='populate_database'),
]
