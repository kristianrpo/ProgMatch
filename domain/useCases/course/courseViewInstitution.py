# domain/useCases/courseView.py
from django.shortcuts import render, redirect
from domain.entities.course import courseEntity

def courseViewInstitution(request):
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
  {
    "id": 1,
    "name": "Introduction to Programming",
    "description": "Delve into coding fundamentals, covering languages, algorithms, and problem-solving techniques."
  },
  {
    "id": 2,
    "name": "Web Development Essentials",
    "description": "Learn to build and deploy interactive websites using HTML, CSS, and JavaScript."
  },
  {
    "id": 3,
    "name": "Data Structures & Algorithms",
    "description": "Understand how to efficiently organize and manipulate data with advanced programming concepts."
  },
  {
    "id": 4,
    "name": "Software Engineering Principles",
    "description": "Gain insights into the software development lifecycle, including design, development, testing, and maintenance."
  },
  {
    "id": 5,
    "name": "Database Management",
    "description": "Explore relational databases, SQL, and data modeling to manage and analyze large datasets."
  },
  {
    "id": 6,
    "name": "Cybersecurity Fundamentals",
    "description": "Learn about protecting information systems from theft or damage to hardware, software, and data."
  },
  {
    "id": 7,
    "name": "Cloud Computing Basics",
    "description": "Get acquainted with cloud services, deployment models, and infrastructure-as-a-service offerings."
  },
  {
    "id": 8,
    "name": "Artificial Intelligence Introduction",
    "description": "An overview of AI principles, machine learning algorithms, and their real-world applications."
  },
  {
    "id": 9,
    "name": "Mobile App Development",
    "description": "Create mobile applications for Android and iOS, understanding the user interface, user experience, and backend processes."
  },
  {
    "id": 10,
    "name": "Network Administration",
    "description": "Study the configuration, management, and operation of computer networks and associated services."
  }
]
    return render(request, 'course/courses.html', {'courses': courses})
