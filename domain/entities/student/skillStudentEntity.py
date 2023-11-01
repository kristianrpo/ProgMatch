from django.db import models
from .studentEntity import student
class skillStudent(models.Model):
    idSkillStudent = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    idStudent = models.ForeignKey(student, on_delete=models.CASCADE)

    class Meta:
        app_label = "student"

    def __str__(self):
        return f"Skill {self.skillStudent.name}"