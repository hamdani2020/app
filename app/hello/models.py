from django.db import models


# Create your models here.
class Item(models.Model):
    """Model class"""

    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        """String representation"""
        return self.name
