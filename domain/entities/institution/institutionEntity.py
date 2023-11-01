from django.db import models

class institution(models.Model):
    idInstitution = models.AutoField(primary_key=True)
    institutionCode = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    class Meta:
        app_label = "institution"
        
    def __str__(self):
        return f"Institution {self.institution.name}"