# sign_up.py
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class signUpOptions(TemplateView):
    template_name = 'authentication/signUpOptions.html'