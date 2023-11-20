from .createLearningPath import categorizeCourses
from django.shortcuts import render
from domain.entities.course.courseEntity import course


def viewLearningPath(request):
    if request.method == "GET":
        description = request.GET.get('description','')
        difficulty = request.GET.get('option','')
        temporaryDatabase = course.objects.all()
        recommended = categorizeCourses(temporaryDatabase, difficulty, description)
        dictionary = {}
        dictionary['userObject'] = request.user
        dictionary['courses'] = recommended
        return render(request,'learningPath/viewLearningPath.html',dictionary)