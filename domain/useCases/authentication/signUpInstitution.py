from django.views.generic import CreateView
from domain.entities.authentication.userEntity import user
from components.authentication.forms import institutionForm
from domain.entities.institution.institutionEntity import institution
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import login

class singUpInsitution(CreateView):
    """
    View for user signup as an institution.

    This class-based view handles the registration of institutions. It uses a form to collect
    information about the institution and the user account. Upon successful registration,
    the user is logged in and redirected.

    Attributes
    ----------
    template_name: str 
        The template to be used for rendering the signup form.
    model: class
        The user model to be used for registration.
    form_class: class
        The form class to collect institution and user information.

    Methods:
        - form_valid(form): 
            Custom logic for handling form submission, including user and institution registration and user login.
    """
    template_name = "authentication/signUpInstitution.html"
    model = user
    form_class = institutionForm
    def form_valid(self,form):
        form.instance.type = 'institution'
        userObject = form.save()
        login(self.request, userObject)
        institutionObject = institution(
            institutionCode=form.cleaned_data['institutionCode'], 
            name=form.cleaned_data['username'],  
            email=form.cleaned_data['email'],  
            password=form.cleaned_data['password1'],  
            description=form.cleaned_data['description']  
        )
        institutionObject.save()
        return redirect(reverse_lazy('homeApp:viewHomePage'))
