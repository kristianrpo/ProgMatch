from django.db import models
class institution(models.Model):
    """
    Django model representing an institution entity.

    This model defines the attributes and behavior of an institution, including its code, name, email, password,
    and description.

    Attributes
    ----------
        - institutionCode: str
            A character field representing the institution code.
        - name: str (primary_key)
            A character field serving as the primary key and representing the name of the institution.
        - email: str
            A character field representing the email address of the institution.
        - password: str
            A character field representing the password associated with the institution.
        - description: str
            A character field providing a brief description of the institution.

    Meta
    ----
        - app_label: str
            The label for the institution app.

    Methods
    -------
        - __str__():
            Returns a string representation of the institution instance, displaying the institution name.

    """
    institutionCode = models.CharField(max_length=45)
    name = models.CharField(max_length=45, primary_key = True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    class Meta:
        app_label = "institution"
        
    def __str__(self):
        return f"Institution {self.name}"