from django.db import models


class BaseModel(models.Model):
    """
    Abstract model which can be inherited
    to create all other models in the project.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
