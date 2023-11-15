from django.db import models
from domain.entities.student.interestEntity import interest
from domain.entities.student.skillStudentEntity import skillStudent
class student(models.Model):
    idStudent = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    age = models.IntegerField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=45)
    interest = models.ManyToManyField(interest)
    skill = models.ManyToManyField(skillStudent)
    class Meta:
        app_label = "student"

    def __str__(self):
        return f"Name {self.name}"