from django.views.generic import CreateView
from domain.entities.authentication.userEntity import user
from components.authentication.forms import studentForm
from domain.entities.student.studentEntity import student
from domain.entities.student.skillStudentEntity import skillStudent
from domain.entities.student.interestEntity import interest
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import login

class signUpStudent(CreateView):
    """
    View for user signup as an student.

    This class-based view handles the registration of students. It uses a form to collect
    information about the student and the user account. Upon successful registration,
    the user is logged in and redirected.

    Attributes
    ----------
    template_name: str 
        The template to be used for rendering the signup form.
    model: class
        The user model to be used for registration.
    form_class: class
        The form class to collect student and user information.

    Methods:
        - form_valid(form): 
            Custom logic for handling form submission, including user and student registration and user login.
    """
    template_name = "authentication/signUpStudent.html"
    model = user
    form_class = studentForm
    def form_valid(self,form):
        form.instance.type = 'student'
        userObject = form.save()
        login(self.request, userObject)
        skillObject = skillStudent(
            name = form.cleaned_data['skills']
        )
        skillObject.save()

        interestObject = interest(
            name = form.cleaned_data['interest']
        )
        interestObject.save()

        studentObject = student(
            idStudent = userObject.id,
            name=form.cleaned_data['username'],
            age=form.cleaned_data['age'], 
            email=form.cleaned_data['email'],  
            password=form.cleaned_data['password1'],  
        )
        studentObject.save()
        studentObject.interest.add(interestObject)
        studentObject.skill.add(skillObject)
        studentObject.save()

        return redirect(reverse_lazy('homeApp:viewHomePage'))
