from django.urls import path
from domain.useCases.course.courseViewInstitution import courseViewInstitution
from domain.useCases.course.courseEditView import courseEditView
from domain.useCases.course.courseDeleteView import courseDeleteView
from domain.useCases.course.courseCreateView import courseCreateView
from domain.useCases.course.courseDetailView import courseDetailView

from domain.useCases.course.addCourses import populate_database
app_name = "courseApp"
urlpatterns = [
    path('courseViewInstitution/<pk>',courseViewInstitution.as_view(),name = "courseViewInstitution"),
    path('courseEditView/<pk>',courseEditView.as_view(),name = "courseEditView"),
    path('courseDeleteView/<pk>',courseDeleteView.as_view(),name = "courseDeleteView"),
    path('courseCreateView/',courseCreateView.as_view(),name = "courseCreateView"),
    path('populate_database/',populate_database,name = "populate_database"),
    path('courseDetailView/<pk>',courseDetailView.as_view(),name = 'courseDetailView'),
]
