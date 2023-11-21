from django.db import models
from domain.entities.student.studentEntity import student
from domain.entities.course.courseEntity import course
from domain.entities.learningPath.skillLearningPathEntity import skillLearningPath
from domain.entities.learningPath.tagsEntity import tags

class learningPath(models.Model):
    """
    Django model representing a learning path entity.

    This model defines the attributes and behavior of a learning path, including its unique identifier,
    name, professional role, path score, associated student, related courses, skills, and tags.

    Attributes
    ----------
        - idlearningPath: AutoField (primary_key)
            An automatically incrementing integer field serving as the primary key.
        - name: str
            A character field representing the name of the learning path.
        - professionalRole: str
            A character field representing the professional role associated with the learning path.
        - pathScore: float
            A floating-point field representing the score of the learning path.
        - idStudent: ForeignKey
            A foreign key linking the learning path to the student who created it.
        - course: ManyToManyField
            A many-to-many relationship field linking the learning path to related courses.
        - skill: ManyToManyField
            A many-to-many relationship field linking the learning path to related skills.
        - tag: ManyToManyField
            A many-to-many relationship field linking the learning path to related tags.

    Meta
    ----
        - app_label: str
            The label for the learning path app.

    Methods
    -------
        - __str__():
            Returns a string representation of the learning path instance, displaying the path name.

    """
    idlearningPath = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    professionalRole = models.CharField(max_length=45)
    pathScore = models.FloatField()
    idStudent = models.ForeignKey(student, on_delete=models.CASCADE)
    course  =  models.ManyToManyField(course)
    skill  =  models.ManyToManyField(skillLearningPath)
    tag =  models.ManyToManyField(tags)
    class Meta:
        app_label = "learningPath"

    def __str__(self):
        return f"Path {self.name}"