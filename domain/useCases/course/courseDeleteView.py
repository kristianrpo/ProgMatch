from django.views.generic.edit import DeleteView
from domain.entities.course.courseEntity import course
from django.urls import reverse_lazy

class courseDeleteView(DeleteView):
    model = course
    template_name = 'course/courseDeleteView.html'
    
    def get_success_url(self):
        return reverse_lazy('courseApp:courseViewInstitution', kwargs={'pk': self.object.idInstitution})
