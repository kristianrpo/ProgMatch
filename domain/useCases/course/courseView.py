# domain/useCases/courseView.py
from django.shortcuts import render, redirect
from domain.entities.course import courseEntity

def courseView(request):
    # if request.user.is_authenticated:
    #     if hasattr(request.user, 'student'):
    #         # If the user is a student, show courses related to their learning path
    #         courses = courseEntity.objects.filter(learning_path=request.user.student.learning_path)
    #     else:
    #         # If the user is not a student, show all courses
    #         courses = courseEntity.objects.all()
    # else:
    #     # If the user is not authenticated, redirect to login page
    #     return redirect('viewHomePage')

    ## Create dummy data
    courses = [
        {'id': 1, 'name': 'Introduction to Biology', 'description': 'Learn about the fundamentals of biology...'},
        {'id': 2, 'name': 'Principles of Chemistry', 'description': 'Dive into the basics of chemical reactions...'},
        {'id': 3, 'name': 'World History', 'description': 'Explore the major events that shaped the world...'},
        {'id': 1, 'name': 'Introduction to Biology', 'description': 'Learn about the fundamentals of biology...'},
        {'id': 2, 'name': 'Principles of Chemistry', 'description': 'Dive into the basics of chemical reactions...'},
        {'id': 3, 'name': 'World History', 'description': 'Explore the major events that shaped the world...'},
        {'id': 1, 'name': 'Introduction to Biology', 'description': 'Learn about the fundamentals of biology...'},
        {'id': 2, 'name': 'Principles of Chemistry', 'description': 'Dive into the basics of chemical reactions...'},
        {'id': 3, 'name': 'World History', 'description': 'Explore the major events that shaped the world...'},
        {'id': 1, 'name': 'Introduction to Biology', 'description': 'Learn about the fundamentals of biology...'},
        {'id': 2, 'name': 'Principles of Chemistry', 'description': 'Dive into the basics of chemical reactions...'},
        {'id': 3, 'name': 'World History', 'description': 'Explore the major events that shaped the world...'},
        # ... add as many courses as you like
    ]
    

    return render(request, 'course/course.html', {'courses': courses})
