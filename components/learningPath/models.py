from django.db import models
from components.student.models import student
# Create your models here.

class learningPath(models.Model):
    idlearningPath = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    professionalRole = models.CharField(max_length=45)
    pathScore = models.FloatField()
    idStudent = models.ForeignKey(student, on_delete=models.CASCADE)

    def __str__(self):
        return f"Path {self.learningPath.name}"
    
class tags(models.Model):
    idTags = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    idLearningPath = models.ForeignKey(learningPath, on_delete=models.CASCADE)
    def __str__(self):
        return f"Tag {self.tags.name}"
    
class skillLearningPath(models.Model):
    idSkills = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    idLearningPath = models.ForeignKey(learningPath,on_delete=models.CASCADE)
    def __str__(self):
        return "Skill {self.skillLearningPath.name}"
    
