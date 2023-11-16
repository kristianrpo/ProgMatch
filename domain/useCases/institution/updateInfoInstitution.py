from django.views.generic import UpdateView
from domain.entities.institution.institutionEntity import institution
from django.contrib.auth.password_validation import validate_password
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseServerError
from django.urls import reverse_lazy
from django.contrib.auth import login
class updateInfoInstitution(UpdateView,LoginRequiredMixin):
    """
    Django class-based view for updating institution information and password.

    This view extends Django's `UpdateView` and includes `LoginRequiredMixin` to ensure that only authenticated users
    can access it.

    Attributes
    -----------
        - model: class
            The model class representing the institution entity.
        - template_name: str
            The HTML template used to render the institution information.
        - fields: tuple 
            The fields that can be updated in the institution.

    Methods
    -------
        - get_context_data(self, **kwargs): 
            Overrides the base method to add additional context data.
        - get(self, request, *args, **kwargs): 
            Overrides the base method to handle GET requests.
        - form_valid(self, form): 
            Overrides the base method to handle form validation and updates.
        - get_success_url(self): 
            Defines the URL to redirect to after a successful update.

    Usage
    ------
        This view allows authenticated users to update their institution information, including name, description,
        institution code, and email. It also provides the ability to change the password.

        The view checks if the institution name matches the logged-in user's username. If not, it returns an HTTP 500
        Internal Server Error response.

        When updating the institution name or email, it also updates the associated user model. If a new password is
        provided, it validates and updates both the user's and institution's passwords.

        If the update is successful, the view redirects to the 'viewInfoInstitution' page for the updated institution.

    """
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
                    messages.error(self.request, 'The new password is not secure.')
                    return redirect('institutionApp:updateInfoInstitution', pk=self.request.user.username)
            else:
                messages.error(self.request, 'The old password is incorrect.')
                return redirect('institutionApp:updateInfoInstitution', pk=self.request.user.username)
        return super().form_valid(form)
    
    def get_success_url(self):
        userActual = self.request.user
        success_url = reverse_lazy('institutionApp:viewInfoInstitution', kwargs={'pk': userActual.username})
        return success_url
    