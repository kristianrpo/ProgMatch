# domain/useCases/courseView.py
from django.shortcuts import render, redirect
from domain.entities.course import courseEntity

def courseView(request, idCourse):
    ## Create the view for an specific course with the id routing

    course = courseEntity.objects.get(idCourse=idCourse)
    return render(request, 'course/course.html', {'course': course})