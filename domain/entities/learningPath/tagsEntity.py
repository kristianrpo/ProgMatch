from django.db import models

class tags(models.Model):
    """
    Django model representing a tag associated with a learning path.

    This model defines the attributes and behavior of a tag, including its unique identifier
    and name.

    Attributes
    ----------
        - idTags: AutoField (primary_key)
            An automatically incrementing integer field serving as the primary key.
        - name: str
            A character field representing the name of the tag.

    Meta
    ----
        - app_label: str
            The label for the learning path app.

    Methods
    -------
        - __str__():
            Returns a string representation of the tag instance, displaying the tag name.

    """
    idTags = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)


    class Meta:
        app_label = "learningPath"

    def __str__(self):
        return f"Tag {self.name}"