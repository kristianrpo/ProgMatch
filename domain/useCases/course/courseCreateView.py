from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from domain.entities.course.courseEntity import course
from domain.entities.institution.institutionEntity import institution
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

class courseCreateView(LoginRequiredMixin, CreateView):
    model = course
    fields = ['courseCode', 'name', 'length', 'price', 'modality', 'content', 'description', 'link', 'difficulty']
    template_name = 'course/courseCreateView.html'
    success_url = reverse_lazy('courseApp:courseCreateView')

    def form_valid(self, form):
        username = self.request.user.username

        try:
            user_institution = institution.objects.get(name=username)
        except institution.DoesNotExist:
            return super().form_invalid(form)

        form.instance.idInstitution = user_institution
        return super().form_valid(form)

    def get_success_url(self):
        institution_pk = self.object.idInstitution.pk

        return reverse('courseApp:courseViewInstitution', kwargs={'pk': institution_pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userObject'] = self.request.user   
        return context