from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
class viewHomeStudent(TemplateView,LoginRequiredMixin):
    template_name = 'student/studentHomePage.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userObject'] = self.request.user
        return context