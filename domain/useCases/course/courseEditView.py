from django.views.generic.edit import UpdateView
from domain.entities.course.courseEntity import course

class courseEditView(UpdateView):
    model = course
    fields = ['courseCode', 'name', 'length', 'price', 'modality', 'content', 'description', 'link', 'difficulty']
    template_name = 'course/courseEditView.html'
    success_url = 'course/courseViewInstitution.html'
