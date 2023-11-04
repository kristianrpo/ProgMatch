from django.views.generic import TemplateView

class signUpOptions(TemplateView):
    """
    View for displaying user signup options.

    This class-based view displays a template that provides options for user registration.
    It serves as a starting point for users to choose their registration path, differentiating
    between student and institution registration.

    Attributes
    ----------
    template_name: str 
        The template to be used for rendering the signup options page.
    """
    template_name = 'authentication/signUpOptions.html'