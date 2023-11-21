from django.db import models
from domain.entities.student.studentEntity import student
from domain.entities.course.courseEntity import course

class review(models.Model):
    """
    Django model representing a review entity for a course.

    This model defines the attributes and behavior of a review, including its unique identifier,
    score, content, creation date, modification date (nullable), associated student, and associated course.

    Attributes
    ----------
        - idReview: AutoField (primary_key)
            An automatically incrementing integer field serving as the primary key.
        - score: IntegerField
            An integer field representing the score assigned to the course by the student.
        - content: TextField
            A text field containing the detailed content of the review.
        - creationDate: DateField
            A date field indicating the creation date of the review.
        - modificationDate: DateField (nullable)
            A date field indicating the modification date of the review (nullable).
        - idStudent: ForeignKey
            A foreign key linking the review to the student who created it.
        - idCourse: ForeignKey
            A foreign key linking the review to the course it is associated with.

    Meta
    ----
        - app_label: str
            The label for the course app.

    Methods
    -------
        - __str__():
            Returns a string representation of the review instance, displaying the review content.

    """

    idReview = models.AutoField(primary_key=True)
    score = models.IntegerField()
    content = models.TextField()
    creationDate = models.DateField()
    modificationDate = models.DateField(null = True)
    idStudent = models.ForeignKey(student, on_delete=models.CASCADE)
    idCourse = models.ForeignKey(course, on_delete=models.CASCADE)

    class Meta:
        app_label = "course"

    def __str__(self):
        return f"Review {self.content}"