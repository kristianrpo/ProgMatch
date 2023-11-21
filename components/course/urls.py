from django.urls import path
from domain.useCases.course.courseViewInstitution import courseViewInstitution
from domain.useCases.course.courseEditView import courseEditView
from domain.useCases.course.courseDeleteView import courseDeleteView
from domain.useCases.course.courseCreateView import courseCreateView
from domain.useCases.course.courseDetailView import courseDetailView


app_name = "courseApp"
urlpatterns = [
    path('courseViewInstitution/<pk>',courseViewInstitution.as_view(),name = "courseViewInstitution"),
    path('courseEditView/<pk>',courseEditView.as_view(),name = "courseEditView"),
    path('courseDeleteView/<pk>',courseDeleteView.as_view(),name = "courseDeleteView"),
    path('courseCreateView/',courseCreateView.as_view(),name = "courseCreateView"),
    path('courseDetailView/<pk>',courseDetailView.as_view(),name = 'courseDetailView'),
]
