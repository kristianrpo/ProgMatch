from django.contrib.auth.models import AbstractUser
from django.db import models

class user(AbstractUser):
    type = models.CharField(max_length=30)
    class Meta:
        app_label = "authentication"
    def __str__(self):
        return f"User {self.id}"