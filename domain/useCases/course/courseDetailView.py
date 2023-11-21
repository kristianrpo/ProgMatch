from django.views.generic import DetailView
from domain.entities.course.courseEntity import course
from django.contrib.auth.mixins import LoginRequiredMixin

class courseDetailView(LoginRequiredMixin, DetailView):
    """
    A class-based view that provides the details of a specific course instance.

    Inherits from `LoginRequiredMixin` to ensure that the view is accessible only to authenticated users,
    and from `DetailView` to provide a detailed view for an object.

    Attributes
    ----------
    model : class
        The model that this view will display. This should be the `course` model, which represents the courses
        in the system.
        
    template_name : str
        The path to the HTML template used for rendering the detailed view of the course.
        
    context_object_name : str
        The name of the context object used in the template to represent the course instance.

    Methods
    -------
    get_context_data(self, **kwargs):
        Extends the superclass method to add the user object to the template context, allowing the template
        to access the currently logged-in user's information.

        Parameters
        ----------
        **kwargs : dict
            Additional keyword arguments passed to the method.

        Returns
        -------
        dict
            The context dictionary with additional information about the user.

    Usage
    -----
    This view is intended to be used when a user wants to view the full details of a specific course. It should
    be mapped to a URL pattern that includes the course's primary key or slug to identify the specific course
    to be detailed.

    Example
    -------
    urlpatterns = [
        path('course/detail/<int:pk>/', courseDetailView.as_view(), name='course-detail'),
    ]
    
    Upon accessing the detail view URL for a particular course, the view fetches the course instance
    from the database and renders it using the 'course/courseDetailView.html' template. The logged-in user's
    information is also included in the context for potential use in the template.
    """
    model = course
    template_name = 'course/courseDetailView.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userObject'] = self.request.user   
        return context