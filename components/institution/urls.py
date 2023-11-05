from django.urls import path
from domain.useCases.institution.viewInfoInstitution import viewInfoInstitution
from domain.useCases.institution.updateInfoInstitution import updateInfoInstitution
from domain.useCases.institution.deleteInstitution import deleteInstitution
app_name = "institutionApp"
urlpatterns = [
    path('viewInfoInstitution/<pk>',viewInfoInstitution.as_view(),name = "viewInfoInstitution"),
    path('updateInfoInstitution/<pk>', updateInfoInstitution.as_view(), name = "updateInfoInstitution"),
    path('deleteInstitution/<pk>', deleteInstitution.as_view(), name = "deleteInstitution")
]