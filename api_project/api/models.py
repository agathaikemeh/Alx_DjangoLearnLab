from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)  # Title field
    author = models.CharField(max_length=100)  # Author field

    def __str__(self):
        return self.title

