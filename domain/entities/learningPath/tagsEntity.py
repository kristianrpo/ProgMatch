from django.db import models

class tags(models.Model):
    idTags = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)


    class Meta:
        app_label = "learningPath"

    def __str__(self):
        return f"Tag {self.name}"