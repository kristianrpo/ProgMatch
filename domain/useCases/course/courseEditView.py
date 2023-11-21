from django.views.generic.edit import UpdateView
from domain.entities.course.courseEntity import course
from django.urls import reverse_lazy

class courseEditView(UpdateView):
    """
    A class-based view for updating an existing course instance.

    Inherits from Django's `UpdateView`, providing a default implementation for updating a specific object.

    Attributes
    ----------
    model : class
        The model that this view will update. It is set to the `course` model, which represents the courses
        in the system.
        
    fields : list
        A list of fields on the `course` model that will be included in the form and can be edited.
        
    template_name : str
        The path to the HTML template used to render the course update form.

    Methods
    -------
    get_success_url(self):
        Determines the URL to redirect to after successfully updating the course instance.
        The user is redirected to the course list view of the institution associated with the course.
        
        Returns
        -------
        str
            A lazy evaluation of the URL named 'courseApp:courseViewInstitution', with the primary key of the
            institution as a URL keyword argument.
        
    get_context_data(self, **kwargs):
        Extends the superclass method to add the user object to the context data, allowing the template
        to access the currently logged-in user's information.
        
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
    This view is intended to be used when an administrator or authorized user wants to edit a course. It should be
    mapped to a URL pattern that includes the course's primary key to identify the specific course to be edited.

    Example
    -------
    urlpatterns = [
        path('course/edit/<int:pk>/', courseEditView.as_view(), name='course-edit'),
    ]
    
    When the edit URL is accessed for a particular course, it presents a form populated with the course's existing data.
    Upon submitting the form, the course instance is updated with the provided data, and the user is redirected to
    the institution's course list view.
    """
    model = course
    fields = ['courseCode', 'name', 'length', 'price', 'modality', 'content', 'description', 'link', 'difficulty']
    template_name = 'course/courseEditView.html'

    def get_success_url(self):
        return reverse_lazy('courseApp:courseViewInstitution', kwargs={'pk': self.object.idInstitution})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userObject'] = self.request.user   
        return context