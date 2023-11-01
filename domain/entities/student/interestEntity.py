from django.db import models
from .studentEntity import student

class interest(models.Model):
    idInterest = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    idStudent = models.ForeignKey(student, on_delete=models.CASCADE)

    class Meta:
        app_label = "student"

    def __str__(self):
        return f"Interest {self.interest.name}"
