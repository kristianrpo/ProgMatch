from django.views.generic import TemplateView
class requestStudent(TemplateView):
    """
    Django class-based view for handling user requests to generate a learning path.

    This view extends Django's `TemplateView` to render a template where users can input their
    description and difficulty level to generate a personalized learning path.

    Attributes
    -----------
        - template_name: str
            The HTML template used to render the request form.

    Methods
    -------
        - get_context_data(self, **kwargs): 
            Override of the base method to add the userObject to the context data.

    Usage
    ------
        This view provides a form for users to input their desired course description and difficulty level.
        It includes the logged-in user object in the context data for the template.
    """
    template_name = 'learningPath/requestStudent.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userObject'] = self.request.user
        return context