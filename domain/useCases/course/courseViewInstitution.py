from django.views.generic import ListView
from domain.entities.institution.institutionEntity import institution
from domain.entities.course.courseEntity import course
from django.contrib.auth.mixins import LoginRequiredMixin

class courseViewInstitution(ListView, LoginRequiredMixin):
    model = course
    template_name = 'course/courseViewInstitution.html'
    context_object_name = 'courses'

    def get_queryset(self):
        institution_id = self.request.user.username
        return course.objects.filter(idInstitution=institution_id) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userObject'] = self.request.user   
        return context

    
    