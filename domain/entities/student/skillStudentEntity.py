from django.db import models


class skillStudent(models.Model):
    """
    Django model representing a skill associated with a student.

    This model defines the attributes and behavior of a skill, including its unique identifier
    and name.

    Attributes
    ----------
        - idSkillStudent: AutoField (primary_key)
            An automatically incrementing integer field serving as the primary key.
        - name: str
            A character field representing the name of the skill.

    Meta
    ----
        - app_label: str
            The label for the student app.

    Methods
    -------
        - __str__():
            Returns a string representation of the skill instance, displaying the skill name.

    """
    idSkillStudent = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    

    class Meta:
        app_label = "student"

    def __str__(self):
        return f"{self.name}"