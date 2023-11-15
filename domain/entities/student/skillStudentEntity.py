from django.db import models


class skillStudent(models.Model):
    idSkillStudent = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    

    class Meta:
        app_label = "student"

    def __str__(self):
        return f"Skill {self.name}"