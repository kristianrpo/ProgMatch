from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
class viewHomeStudent(TemplateView,LoginRequiredMixin):
    """
    Django class-based view for displaying the home page of a student.

    This view extends Django's `TemplateView` and includes `LoginRequiredMixin` to ensure that only authenticated users
    can access it.

    Attributes
    -----------
        - template_name: str
            The HTML template used to render the student home page.

    Methods
    -------
        - get_context_data(self, **kwargs): 
            Overrides the base method to add additional context data.

    Usage
    ------
        This view displays the home page for authenticated students and provides context data containing the logged-in user object.
    """
    template_name = 'student/studentHomePage.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userObject'] = self.request.user
        return context