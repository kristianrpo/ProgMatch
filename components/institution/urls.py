from django.urls import path
from domain.useCases.institution.viewInfoInstitution import viewInfoInstitution
from domain.useCases.institution.updateInfoInstitution import updateInfoInstitution
app_name = "institutionApp"
urlpatterns = [
    path('viewInfoInstitution/<pk>',viewInfoInstitution.as_view(),name = "viewInfoInstitution"),
    path('updateInfoInstitution/<pk>', updateInfoInstitution.as_view(), name = "updateInfoInstitution")
]