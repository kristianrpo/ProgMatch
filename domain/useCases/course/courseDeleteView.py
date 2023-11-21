from django.views.generic.edit import DeleteView
from domain.entities.course.courseEntity import course
from django.urls import reverse_lazy

class courseDeleteView(DeleteView):
    """
    A class-based view for deleting a course instance.

    This view extends Django's `DeleteView` to handle the deletion of course records. It displays a confirmation
    page before the final deletion of the course item.

    Attributes
    ----------
    model : class
        The model that this view will delete instances of. It is set to the `course` model.
        
    template_name : str
        The path to the HTML template this view will use for rendering the deletion confirmation page.

    Methods
    -------
    get_success_url(self):
        Determines the URL to redirect to after successfully deleting the course instance.
        The user is redirected to the course list view of the institution associated with the course.
        
        Returns
        -------
        str
            A lazy evaluation of the URL named 'courseApp:courseViewInstitution', with the primary key of the
            institution as a URL keyword argument.

    get_context_data(self, **kwargs):
        Extends the method to add additional context data to the template.

        Parameters
        ----------
        **kwargs : dict
            Keyword arguments that contain context data.

        Returns
        -------
        dict
            The context data dictionary with the added user object, allowing the template to access the currently
            logged-in user's information.

    Usage
    -----
    This view is intended to be used when an administrator or authorized user wants to delete a course. It should be
    mapped to a URL pattern that includes the course's primary key to identify the specific course to be deleted.

    Example
    -------
    urlpatterns = [
        path('course/delete/<int:pk>/', courseDeleteView.as_view(), name='course-delete'),
    ]
    
    When the delete URL is accessed for a particular course, it presents a confirmation page. Upon confirmation, the
    course is deleted, and the user is redirected to the institution's course list view.
    """
    model = course
    template_name = 'course/courseDeleteView.html'
    
    def get_success_url(self):
        return reverse_lazy('courseApp:courseViewInstitution', kwargs={'pk': self.object.idInstitution})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userObject'] = self.request.user   
        return context