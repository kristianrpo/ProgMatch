from django.views.generic.edit import DeleteView
from domain.entities.course.courseEntity import course
from django.urls import reverse_lazy

class courseDeleteView(DeleteView):
    model = course
    template_name = 'course/courseDeleteView.html'
    success_url = reverse_lazy('courseApp:courseViewInstitution')  # URL to redirect after a successful delete
