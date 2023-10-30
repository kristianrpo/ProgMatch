from django.db import models

# Create your models here.
class institution(models.Model):
    idInstitution = models.AutoField(primary_key=True)
    institutionCode = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    def __str__(self):
        return f"Institution {self.institution.name}"