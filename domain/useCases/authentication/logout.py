from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy

def logoutFunction(request):
    """
    View function for user logout.

    This function logs out the currently authenticated user and redirects them to the home page.

    Args
    ----
        request (HttpRequest): The HTTP request object.

    Returns
    -------
        HttpResponse: A redirect to the home page after logging out the user.

    """
    logout(request)
    return redirect(reverse_lazy('homeApp:viewHomePage'))
