from django.db import models

# Represents an Author who can write multiple books
# This model stores details about an author
class Author(models.Model):
    # The name of the author, stored as a string with a maximum length of 100 characters
    name = models.CharField(max_length=100)

    # The __str__ method returns a human-readable representation of the object
    # Here, it returns the name of the author when the object is printed
    def __str__(self):
        return self.name


# Represents a Book with a relationship to an Author
# This model stores details about a book
class Book(models.Model):
    # The title of the book, stored as a string with a maximum length of 200 characters
    title = models.CharField(max_length=200)

    # The year the book was published, stored as an integer
    publication_year = models.IntegerField()

    # A ForeignKey establishes a one-to-many relationship
    # Each book is linked to one Author, but an Author can have multiple books
    # `related_name='books'` allows reverse access from the Author model to retrieve all related books
    # `on_delete=models.CASCADE` ensures that when an Author is deleted, all their books are also deleted
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    # The __str__ method returns a human-readable representation of the object
    # Here, it returns the title of the book when the object is printed
    def __str__(self):
        return self.title


# Models representing an Author and their Books
# Author can have multiple Books; this is a one-to-many relationship
