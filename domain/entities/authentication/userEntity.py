from django.contrib.auth.models import AbstractUser
from django.db import models

class user(AbstractUser):
    """
    Custom User Model with an additional 'type' attribute.

    This custom user model extends Django's AbstractUser model and adds an extra
    field 'type' to categorize the type of user (e.g., 'admin', 'teacher', 'student').

    Attributes:
    ----------
    - type: str
        A text field to specify the type of user.

    Meta:
    -----
    - app_label(str):
        The label for the authentication app.

    Methods:
    --------
    - __str__():
        A method to provide a string representation of the user instance. It returns
        a string containing "User" followed by the user's ID.

    Note: This custom user model is designed to extend Django's built-in user
    authentication system and add a 'type' field for user categorization.

    """
    type = models.CharField(max_length=30)
    class Meta:
        app_label = "authentication"
    def __str__(self):
        return f"User {self.id}"