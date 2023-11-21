from django.db import models
from domain.entities.student.interestEntity import interest
from domain.entities.student.skillStudentEntity import skillStudent
class student(models.Model):
    """
    Django model representing a student entity.

    This model defines the attributes and behavior of a student, including its unique identifier,
    name, age, email, password, interests, and skills.

    Attributes
    ----------
        - idStudent: IntegerField (primary_key)
            An integer field serving as the primary key for the student.
        - name: str
            A character field representing the name of the student.
        - age: IntegerField
            An integer field representing the age of the student.
        - email: str
            A character field representing the email address of the student.
        - password: str
            A character field representing the password associated with the student.
        - interest: ManyToManyField
            A many-to-many relationship field linking the student to their interests.
        - skill: ManyToManyField
            A many-to-many relationship field linking the student to their skills.

    Meta
    ----
        - app_label: str
            The label for the student app.

    Methods
    -------
        - __str__():
            Returns a string representation of the student instance, displaying the student's name.

    """
    idStudent = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    age = models.IntegerField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=45)
    interest = models.ManyToManyField(interest)
    skill = models.ManyToManyField(skillStudent)
    class Meta:
        app_label = "student"

    def __str__(self):
        return f"{self.name}"