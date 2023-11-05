"""
URL Patterns for the 'institutionApp' Django application.

These URL patterns define how different views within the 'institutionApp' should be accessed.
They are responsible for routing requests to the appropriate view classes.

- 'viewInfoInstitution': Matches the URL 'viewInfoInstitution/<pk>' and routes it to the 'viewInfoInstitution' view.
- 'updateInfoInstitution': Matches the URL 'updateInfoInstitution/<pk>' and routes it to the 'updateInfoInstitution' view.
- 'deleteInstitution': Matches the URL 'deleteInstitution/<pk>' and routes it to the 'deleteInstitution' view.

Parameters
-----------
    - 'pk':int 
        The primary key used to identify the institution.
"""

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