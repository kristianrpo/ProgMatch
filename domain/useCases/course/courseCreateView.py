from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from domain.entities.course.courseEntity import course
from django.contrib.auth.mixins import LoginRequiredMixin

class courseCreateView(LoginRequiredMixin, CreateView):
    model = course
    fields = ['courseCode', 'name', 'length', 'price', 'modality', 'content', 'description', 'link', 'difficulty', 'idInstitution']
    template_name = 'course/courseCreateView.html'
    success_url = reverse_lazy('courseApp:courseCreateView')  # Adjust the URL to where you want to redirect after the course is created

    def form_valid(self, form):
        # Assuming you want to automatically set the current user's institution as the course's institution
        form.instance.idInstitution = self.request.username
        return super().form_valid(form)
