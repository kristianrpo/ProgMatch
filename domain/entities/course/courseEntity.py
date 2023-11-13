from django.db import models
from domain.entities.institution.institutionEntity import institution
from domain.entities.learningPath.learningPathEntity import learningPath

class Course(models.Model):
    DIFFICULTY_CHOICES = [
        ('facil', 'Fácil'),
        ('intermedio', 'Intermedio'),
        ('dificil', 'Difícil'),
    ]

    idCourse = models.AutoField(primary_key=True)
    courseCode = models.CharField(max_length=45)
    name = models.CharField(max_length=100)
    length = models.CharField(max_length=45)
    price = models.FloatField()
    modality = models.CharField(max_length=45)
    content = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    idInstitution = models.ForeignKey(institution, on_delete=models.CASCADE)
    idLearningPath = models.ForeignKey(learningPath, on_delete=models.CASCADE)
    link = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)

    def __str__(self):
        return self.name
