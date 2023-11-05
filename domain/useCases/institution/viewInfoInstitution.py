from django.views.generic import DetailView
from domain.entities.institution.institutionEntity import institution
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseServerError
class viewInfoInstitution(DetailView,LoginRequiredMixin):
    """
    Django class-based view for displaying detailed information about an institution.

    This view extends Django's `DetailView` and includes `LoginRequiredMixin` to ensure that only authenticated users
    can access it.

    Attributes
    -----------
        - model : class 
            The model class representing the institution entity.
        - template_name: str
            The HTML template used to render the institution information.
        - context_object_name: str 
            The name used to refer to the institution object in the template.

    Methods
    -------
        - get_context_data(self, **kwargs): 
            Overrides the base method to add additional context data.
        - get(self, request, *args, **kwargs): 
            Overrides the base method to handle GET requests.

    Usage
    -----
        This view displays detailed information about an institution. It checks if the logged-in user has access to
        the institution based on the institution's name matching the user's username.

    If the institution name matches the user's username, it renders the template with the institution details.
    If not, it returns an HTTP 500 Internal Server Error response.

    """
    model = institution
    template_name = 'institution/accountSettings.html'
    context_object_name = 'institutionObject'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userObject'] = self.request.user   
        context['buttonOption'] = 1
        return context
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.name == self.request.user.username:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            return HttpResponseServerError("You don´t have access to this section.")