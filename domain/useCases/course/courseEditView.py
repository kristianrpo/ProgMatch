from django.views.generic.edit import UpdateView
from domain.entities.course.courseEntity import course
from django.urls import reverse_lazy

class courseEditView(UpdateView):
    model = course
    fields = ['courseCode', 'name', 'length', 'price', 'modality', 'content', 'description', 'link', 'difficulty']
    template_name = 'course/courseEditView.html'

    def get_success_url(self):
        return reverse_lazy('courseApp:courseViewInstitution', kwargs={'pk': self.object.idInstitution})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userObject'] = self.request.user   
        return context