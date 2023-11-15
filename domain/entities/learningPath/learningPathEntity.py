from django.db import models
from domain.entities.student.studentEntity import student
from domain.entities.course.courseEntity import course
from domain.entities.learningPath.skillLearningPathEntity import skillLearningPath
from domain.entities.learningPath.tagsEntity import tags

class learningPath(models.Model):
    idlearningPath = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    professionalRole = models.CharField(max_length=45)
    pathScore = models.FloatField()
    idStudent = models.ForeignKey(student, on_delete=models.CASCADE)
    course  =  models.ManyToManyField(course)
    skill  =  models.ManyToManyField(skillLearningPath)
    tag =  models.ManyToManyField(tags)
    class Meta:
        app_label = "learningPath"

    def __str__(self):
        return f"Path {self.name}"