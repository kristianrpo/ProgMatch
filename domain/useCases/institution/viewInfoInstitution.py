from django.views.generic import DetailView
from domain.entities.institution.institutionEntity import institution
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseServerError
class viewInfoInstitution(DetailView,LoginRequiredMixin):
    model = institution
    template_name = 'institution/accountSettings.html'
    context_object_name = 'institutionObject'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userObject'] = self.request.user   
        context['buttonOption'] = 1
        return context
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.name == self.request.user.username:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            return HttpResponseServerError("You don´t have access to this section.")