from django.db import models
from domain.entities.student.studentEntity import student
from domain.entities.course.courseEntity import course

class review(models.Model):
    idReview = models.AutoField(primary_key=True)
    score = models.IntegerField()
    content = models.TextField()
    creationDate = models.DateField()
    modificationDate = models.DateField(null = True)
    idStudent = models.ForeignKey(student, on_delete=models.CASCADE)
    idCourse = models.ForeignKey(course, on_delete=models.CASCADE)

    class Meta:
        app_label = "course"

    def __str__(self):
        return f"Review {self.content}"