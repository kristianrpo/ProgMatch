from django.views.generic import DeleteView
from domain.entities.institution.institutionEntity import institution
from django.http import HttpResponseServerError
from django.urls import reverse_lazy
class deleteInstitution(DeleteView):
    model = institution
    template_name = 'institution/accountSettings.html'
    success_url = reverse_lazy('homeApp:viewHomePage')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userObject'] = self.request.user   
        context['buttonOption'] = 3
        return context
    
    def form_valid(self, form):
        userInstance = self.request.user
        userInstance.delete()
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.name == self.request.user.username:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            return HttpResponseServerError("You don´t have access to this section.")
    