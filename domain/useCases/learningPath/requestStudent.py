from django.views.generic import TemplateView
class requestStudent(TemplateView):
    template_name = 'learningPath/requestStudent.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userObject'] = self.request.user
        return context