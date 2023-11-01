from django.contrib import admin
from domain.entities.course.courseEntity import course
from domain.entities.course.reviewEntity import review

admin.site.register(course)
admin.site.register(review)