from django.db import models
from domain.entities.learningPath.learningPathEntity import learningPath

class tags(models.Model):
    idTags = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    idLearningPath = models.ForeignKey(learningPath, on_delete=models.CASCADE)

    class Meta:
        app_label = "learningPath"

    def __str__(self):
        return f"Tag {self.tags.name}"