from django.views.generic import UpdateView
from domain.entities.institution.institutionEntity import institution
from django.contrib.auth.password_validation import validate_password
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseServerError
from django.urls import reverse_lazy
from django.contrib.auth import login
class updateInfoInstitution(UpdateView,LoginRequiredMixin):
    model = institution
    template_name = 'institution/accountSettings.html'
    fields = ('name','description','institutionCode','email')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userObject'] = self.request.user   
        context['buttonOption'] = 2
        return context
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.name == self.request.user.username:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            return HttpResponseServerError("You don´t have access to this section.")
        
    def form_valid(self, form):
        if form.cleaned_data['name'] != self.request.user.username:
            userInstance = self.request.user
            userInstance.username = form.cleaned_data['name']
            userInstance.save()
        if form.cleaned_data['email'] != self.request.user.email:
            userInstance = self.request.user
            userInstance.email = form.cleaned_data['email']
            userInstance.save()
        if len(self.request.POST.get('oldPassword'))>0 and len(self.request.POST.get('newPassword'))>0:
            userInstance = self.request.user
            if userInstance.check_password(self.request.POST.get('oldPassword')):
                try: 
                    validate_password(self.request.POST.get('newPassword'))
                    userInstance.set_password(self.request.POST.get('newPassword'))
                    userInstance.save()
                    login(self.request, userInstance)

                    institutionInstance = self.object
                    institutionInstance.password = self.request.POST.get('newPassword')
                    institutionInstance.save()
                except:
                    messages.error(self.request, 'La contraseña nueva no es segura')
                    return redirect('institutionApp:updateInfoInstitution', pk=self.request.user.username)
            else:
                messages.error(self.request, 'La contraseña antigua es incorrecta.')
                return redirect('institutionApp:updateInfoInstitution', pk=self.request.user.username)
        return super().form_valid(form)
    
    def get_success_url(self):
        userActual = self.request.user
        success_url = reverse_lazy('institutionApp:viewInfoInstitution', kwargs={'pk': userActual.username})
        return success_url
    