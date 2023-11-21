from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from domain.entities.course.courseEntity import course
from domain.entities.institution.institutionEntity import institution
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

class courseCreateView(LoginRequiredMixin, CreateView):
    """
    A class-based view for creating new course instances within an institution.

    This view allows authenticated users to create new courses by providing the necessary course details.
    Inherits from Django's `CreateView` and `LoginRequiredMixin` to ensure that the view is only accessible
    to authenticated users.

    Attributes
    ----------
    model : class
        The model that this view will create instances of. This should be the `course` model.
        
    fields : list
        A list of fields that will be included in the form presented to the user. These fields are necessary
        for creating a new course instance.
        
    template_name : str
        The path to the HTML template this view will use for rendering the course creation form.
        
    success_url : str
        The URL to redirect to after successful creation of a course instance. Uses `reverse_lazy` to ensure
        it's lazily evaluated to account for any changes in the URLconf.

    Methods
    -------
    form_valid(self, form):
        Processes the form when it is valid. Overrides the superclass method to associate the new course
        with the user's institution and to handle institution lookup failure.

        Parameters
        ----------
        form : ModelForm
            The form instance containing the submitted data.
        
        Returns
        -------
        HttpResponse
            Redirects to the success URL if the form is valid and the course instance has been created successfully.
            Returns a form invalid response if the institution does not exist.
        
    get_success_url(self):
        Overrides the method to dynamically return the success URL, which redirects to the course view page of the
        institution that the created course belongs to.

    get_context_data(self, **kwargs):
        Extends the method to add additional context data to the template.

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
    This view should be mapped to a URL pattern to allow users to access the course creation form. After the user
    submits the form, the new course instance is created and associated with their institution. The user is then
    redirected to the institution's course view page.

    Example
    -------
    urlpatterns = [
        path('course/create/', courseCreateView.as_view(), name='course-create'),
    ]
    
    When the user accesses the course creation page, fills out the form, and submits it, a new course instance
    will be created. The user is redirected to the course list page of the institution if the form is valid.
    If the user's institution is not found, the form submission is considered invalid, and the user remains on the
    course creation form page with an error message.
    """
    model = course
    fields = ['courseCode', 'name', 'length', 'price', 'modality', 'content', 'description', 'link', 'difficulty']
    template_name = 'course/courseCreateView.html'
    success_url = reverse_lazy('courseApp:courseCreateView')

    def form_valid(self, form):
        username = self.request.user.username

        try:
            user_institution = institution.objects.get(name=username)
        except institution.DoesNotExist:
            return super().form_invalid(form)

        form.instance.idInstitution = user_institution
        return super().form_valid(form)

    def get_success_url(self):
        institution_pk = self.object.idInstitution.pk

        return reverse('courseApp:courseViewInstitution', kwargs={'pk': institution_pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userObject'] = self.request.user   
        return context