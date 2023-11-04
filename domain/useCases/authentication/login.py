from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
def loginFunction(request):
    """
    View function for user login.

    This function handles the user login process. It checks if the request method is POST,
    and if so, attempts to authenticate the user. If authentication is successful, the user is
    logged in and redirected. If authentication fails, an error message is
    displayed on the login page.

    Args
    ------
        request (HttpRequest): The HTTP request object.

    Returns
    -------
        HttpResponse: A redirect if login is successful, or a rendered
        login page again with an error message if login fails.

    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('homeApp:viewHomePage'))
        else:
            return render(request, 'authentication/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'authentication/login.html')
