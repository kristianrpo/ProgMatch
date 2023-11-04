from django.db import models
from .studentEntity import student

class petition(models.Model):
    idPetition = models.AutoField(primary_key=True)
    level = models.IntegerField()
    topic = models.CharField(max_length=45)
    description = models.CharField(max_length=200)
    goal = models.CharField(max_length=200)
    idStudent = models.ForeignKey(student, on_delete=models.CASCADE)

    class Meta:
        app_label = "student"

    def __str__(self):
        return f"Petition for {self.description}"
    