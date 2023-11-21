from django.views.generic import DetailView
from domain.entities.course.courseEntity import course
from django.contrib.auth.mixins import LoginRequiredMixin

class courseDetailView(LoginRequiredMixin, DetailView):
    model = course
    template_name = 'course/courseDetailView.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userObject'] = self.request.user   
        return context