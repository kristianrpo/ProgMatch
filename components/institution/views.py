from django.shortcuts import render
from django.views.generic import TemplateView

class ModelView(TemplateView):
    template_name = "institution/institution.html"

# Create your views here.
