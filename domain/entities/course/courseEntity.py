from django.db import models
from domain.entities.institution.institutionEntity import institution

class course(models.Model):
    """
    Django model representing a course entity.

    This model defines the attributes and behavior of a course, including its code, name, length,
    price, modality, content, description, associated institution, link, and difficulty level.

    Attributes
    ----------
        - courseCode: str
            A character field representing the course code.
        - name: str
            A character field representing the course name.
        - length: str
            A character field representing the length or duration of the course.
        - price: float
            A floating-point field representing the price of the course.
        - modality: str
            A character field representing the modality of the course.
        - content: str (nullable)
            A character field representing the content of the course (nullable).
        - description: str
            A text field providing a detailed description of the course.
        - idInstitution: ForeignKey
            A foreign key linking the course to an associated institution.
        - link: str
            A character field representing the link or URL of the course.
        - difficulty: str
            A character field representing the difficulty level of the course,
            selected from predefined choices.

    Meta
    ----
        - app_label: str
            The label for the course app.

    Methods
    -------
        - __str__():
            Returns a string representation of the course instance, displaying the course name.

    """
    DIFFICULTY_CHOICES = [
        ('easy', 'easy'),
        ('intermediate', 'intermediate'),
        ('difficult', 'difficult'),
    ]

    courseCode = models.CharField(max_length=45)
    name = models.CharField(max_length=100)
    length = models.CharField(max_length=45)
    price = models.FloatField()
    modality = models.CharField(max_length=45)
    content = models.CharField(max_length=200, null=True)
    description = models.TextField()
    idInstitution = models.ForeignKey(institution, on_delete=models.CASCADE)
    link = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=100, choices=DIFFICULTY_CHOICES)


    class Meta:
        app_label= "course"
    def __str__(self):
        return self.name
