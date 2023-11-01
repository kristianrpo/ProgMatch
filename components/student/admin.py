from django.contrib import admin
from domain.entities.student.studentEntity import student
from domain.entities.student.skillStudentEntity import skillStudent
from domain.entities.student.petitionEntity import petition
from domain.entities.student.interestEntity import interest

admin.site.register(student)
admin.site.register(skillStudent)
admin.site.register(petition)
admin.site.register(interest)