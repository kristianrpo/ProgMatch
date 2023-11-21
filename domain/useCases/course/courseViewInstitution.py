from django.views.generic import ListView
from domain.entities.institution.institutionEntity import institution
from domain.entities.course.courseEntity import course
from django.contrib.auth.mixins import LoginRequiredMixin

class courseViewInstitution(ListView, LoginRequiredMixin):
    """
    A class-based view that lists all course instances associated with a specific institution.

    This view extends Django's `ListView`, providing a page with a list of courses. `LoginRequiredMixin`
    is used to ensure that only authenticated users can access the view.

    Attributes
    ----------
    model : class
        The model that this view will display. Set to the `course` model, representing the courses in the system.

    template_name : str
        The path to the HTML template used to render the list of courses.

    context_object_name : str
        The name of the context object used in the template to represent the list of courses.

    Methods
    -------
    get_queryset(self):
        Overrides the method to return a queryset that is filtered to only include courses associated
        with the institution of the currently logged-in user.

        Returns
        -------
        QuerySet
            A queryset of `course` instances that are associated with the user's institution.
        
    get_context_data(self, **kwargs):
        Extends the method to add the user object to the context data, allowing the template to access
        the currently logged-in user's information.

        Parameters
        ----------
        **kwargs : dict
            Keyword arguments that contain context data.

        Returns
        -------
        dict
            The context data dictionary with the added user object.

    Usage
    -----
    This view is intended to be used by institution administrators or staff to see a list of courses offered
    by their institution. It should be mapped to a URL pattern that is accessible only to authenticated users.

    Example
    -------
    urlpatterns = [
        path('institution/courses/', courseViewInstitution.as_view(), name='institution-courses'),
    ]
    
    Upon accessing the URL, the view will present a list of courses related to the institution that the
    currently logged-in user is associated with. The user's details are also included in the context for
    potential use in the template.
    """
    model = course
    template_name = 'course/courseViewInstitution.html'
    context_object_name = 'courses'

    def get_queryset(self):
        institution_id = self.request.user.username
        return course.objects.filter(idInstitution=institution_id) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userObject'] = self.request.user   
        return context
