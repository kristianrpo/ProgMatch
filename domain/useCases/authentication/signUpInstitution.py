from django.views.generic import CreateView
from domain.entities.authentication.userEntity import user
from components.authentication.forms import institutionForm
from domain.entities.institution.institutionEntity import institution
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login

class singUpInsitution(CreateView):
    template_name = "authentication/signUpInstitution.html"
    model = user
    form_class = institutionForm
    def form_valid(self,form):
        form.instance.type = 'institution'
        userObject = form.save()
        print(userObject)
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
