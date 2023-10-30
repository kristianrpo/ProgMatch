from django.db import models
from components.institution.models import institution
from components.learningPath.models import learningPath
from components.student.models import student

# Create your models here.
class course(models.Model):
    idCourse = models.AutoField(primary_key=True)
    courseCode = models.CharField(max_length=45)
    name = models.CharField(max_length=100)
    length = models.CharField(max_length=45)
    price = models.FloatField()
    modality = models.CharField(max_length=45)
    content = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null = True)
    idInstitution = models.ForeignKey(institution, on_delete=models.CASCADE)
    idLearningPath = models.ForeignKey(learningPath, on_delete=models.CASCADE)
    def __str__(self):
        return f"Course {self.course.name}"
    
class review(models.Model):
    idReview = models.AutoField(primary_key=True)
    score = models.IntegerField()
    content = models.CharField(max_length=200)
    creationDate = models.DateField()
    modificationDate = models.DateField(null = True)
    idStudent = models.ForeignKey(student, on_delete=models.CASCADE)
    idCourse = models.ForeignKey(course, on_delete=models.CASCADE)
    def __str__(self):
        return f"Review {self.review.content}"