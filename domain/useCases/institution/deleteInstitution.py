from django.views.generic import DeleteView
from domain.entities.institution.institutionEntity import institution
from django.http import HttpResponseServerError
from django.urls import reverse_lazy
class deleteInstitution(DeleteView):
    """
    Django class-based view for deleting an institution.

    This view extends Django's `DeleteView` and provides the functionality to delete an institution entity.

    Attributes
    ----------
        - model: class 
            The model class representing the institution entity.
        - template_name: str 
            The HTML template used to confirm the deletion.
        - success_url: str
            The URL to redirect to after successful deletion.

    Methods
    -------
        - get_context_data(self, **kwargs): 
            Overrides the base method to add additional context data.
        - form_valid(self, form): 
            Overrides the base method to handle form validation and deletion.
        - get(self, request, *args, **kwargs): 
            Overrides the base method to handle GET requests.

    Usage:
        This view allows authenticated users to delete their institution. It confirms the deletion and, upon success,
        redirects the user to the home page.

        The view checks if the institution name matches the logged-in user's username. If not, it returns an HTTP 500
        Internal Server Error response.
    """
    model = institution
    template_name = 'institution/accountSettings.html'
    success_url = reverse_lazy('homeApp:viewHomePage')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userObject'] = self.request.user   
        context['buttonOption'] = 3
        return context
    
    def form_valid(self, form):
        userInstance = self.request.user
        userInstance.delete()
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.name == self.request.user.username:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            return HttpResponseServerError("You don´t have access to this section.")
    