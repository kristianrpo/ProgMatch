from django.views.generic import TemplateView

class viewHome(TemplateView):
    """
    Generic Django class that allows you to connect to a template and view its contents.

    ...
    Attributes
    ----------
    template_name : str
        path where the template to be displayed is located.
    """
    
    template_name = "home/home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userObject'] = self.request.user    
        print(context['userObject'])
        return context