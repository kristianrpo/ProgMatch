from .createLearningPath import categorizeCourses
from django.shortcuts import render
from domain.entities.course.courseEntity import course


def viewLearningPath(request):
    """
    Django view for displaying a learning path based on user preferences.

    This view takes input parameters from a GET request, including 'description' and 'option' (for difficulty).
    It then utilizes the categorizeCourses function to filter and recommend courses from the database accordingly.

    Parameters
    ----------
        request: HttpRequest
            The HTTP request object.

    Returns
    -------
        HttpResponse
            A response containing the rendered HTML template displaying the learning path.

    Usage
    ------
        This view is designed to be accessed through a GET request, where the user provides parameters such as
        'description' and 'option' to customize the learning path. The recommended courses are then displayed
        along with the userObject in the template.
    """
    if request.method == "GET":
        description = request.GET.get('description','')
        difficulty = request.GET.get('option','')
        temporaryDatabase = course.objects.all()
        recommended = categorizeCourses(temporaryDatabase, difficulty, description)
        dictionary = {}
        dictionary['userObject'] = request.user
        dictionary['courses'] = recommended
        return render(request,'learningPath/viewLearningPath.html',dictionary)