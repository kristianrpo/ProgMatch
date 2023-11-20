from .createLearningPath import categorizeCourses
from django.shortcuts import render
def viewLearningPath(request):
    if request.method == "GET":
        description = request.GET.get('description','')
        difficulty = request.GET.get('option','')
        temporaryDatabase = {
            "C001": {
                "name": "Introduction to Programming",
                "length": "8 weeks",
                "price": 49.99,
                "modality": "Online",
                "content": "Basic programming concepts",
                "description": "Learn the fundamentals of programming in this introductory course.",
                "idInstitution": 1,
                "link": "https://example.com/courses/c001",
                "difficulty": "easy",
            },
            "C002": {
                "name": "Advanced Algorithms",
                "length": "12 weeks",
                "price": 79.99,
                "modality": "In-person",
                "content": "Advanced algorithms and data structures",
                "description": "Explore advanced algorithms and optimization techniques in this advanced course.",
                "idInstitution": 2,
                "link": "https://example.com/courses/c002",
                "difficulty": "difficult",
            },
            "C003": {
            "name": "Web Development with HTML and CSS",
            "length": "10 weeks",
            "price": 59.99,
            "modality": "Online",
            "content": "Design and development of static web pages",
            "description": "Learn to create attractive web pages using HTML and CSS in this practical course.",
            "idInstitution": 3,
            "link": "https://example.com/courses/c003",
            "difficulty": "intermediate",
            },
            "C004": {
                "name": "Artificial Intelligence for Beginners",
                "length": "6 weeks",
                "price": 39.99,
                "modality": "Online",
                "content": "Basic concepts of Artificial Intelligence",
                "description": "Discover the fundamental concepts of Artificial Intelligence in this beginner-friendly course.",
                "idInstitution": 1,
                "link": "https://example.com/courses/c004",
                "difficulty": "easy",
            },
            "C005": {
                "name": "Object-Oriented Programming with Python",
                "length": "8 weeks",
                "price": 69.99,
                "modality": "Online",
                "content": "Principles of object-oriented programming (OOP) with Python",
                "description": "Master the principles of OOP using Python as the programming language in this advanced course.",
                "idInstitution": 2,
                "link": "https://example.com/courses/c005",
                "difficulty": "intermediate",
            },
            "C006": {
                "name": "Mobile App Development with React Native",
                "length": "14 weeks",
                "price": 89.99,
                "modality": "Online",
                "content": "Construction of cross-platform mobile applications",
                "description": "Learn to develop mobile applications with React Native and address specific challenges of cross-platform development.",
                "idInstitution": 3,
                "link": "https://example.com/courses/c006",
                "difficulty": "difficult",
            }
        }
        recommended = categorizeCourses(temporaryDatabase, difficulty, description)
        lengthLearningPath = 2
        recommended['userObject'] = request.user
        recommended['lengthLearningPath'] = range(1,lengthLearningPath+1)
        print(recommended)
        print(lengthLearningPath)
        return render(request,'learningPath/viewLearningPath.html',recommended)
    