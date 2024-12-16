from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

#documentation
class Author(models.Model):
    """
    The Author model represents an author in the system.
    It contains the name of the author.
    """
    name = models.CharField(max_length=255)

class Book(models.Model):
    """
    The Book model represents a book in the system.
    It contains the title, publication year, and a foreign key to the Author model.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
