from django.db import models

class interest(models.Model):
    idInterest = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        app_label = "student"

    def __str__(self):
        return f"{self.name}"
