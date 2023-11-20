from .createLearningPath import categorizeCourses
from django.shortcuts import render
from domain.entities.course.courseEntity import course


def viewLearningPath(request):
    if request.method == "GET":
        description = request.GET.get('description','')
        difficulty = request.GET.get('option','')
        temporaryDatabase = course.objects.all()
        recommended = categorizeCourses(temporaryDatabase, difficulty, description)
        lengthLearningPath = 2
        recommended['userObject'] = request.user
        recommended['lengthLearningPath'] = range(1,lengthLearningPath+1)
        print(recommended)
        print(lengthLearningPath)
        return render(request,'learningPath/viewLearningPath.html',recommended)
    