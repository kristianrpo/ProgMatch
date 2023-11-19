from django.views.generic import DeleteView
from domain.entities.student.studentEntity import student
from django.http import HttpResponseServerError
from django.urls import reverse_lazy
class deleteStudent(DeleteView):
    """
    Django class-based view for deleting a student.

    This view extends Django's `DeleteView` and provides the functionality to delete an student entity.

    Attributes
    ----------
        - model: class 
            The model class representing the student entity.
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
        This view allows authenticated users to delete their account. It confirms the deletion and, upon success,
        redirects the user to the home page.

        The view checks if the student id matches the logged-in user's id. If not, it returns an HTTP 500
        Internal Server Error response.
    """
    model = student
    template_name = 'student/accountSettings.html'
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
        if self.object.idStudent == self.request.user.id:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            return HttpResponseServerError("You don´t have access to this section.")
    