# CRUD Operations in Django Shell

## Create Operation
```python
# Command to create a book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Expected Output
# <Book: 1984>
# Command to retrieve the book instance
book = Book.objects.get(title="1984")
# Expected Output
# <Book: 1984>
# book.title, book.author, book.publication_year will display:
# '1984', 'George Orwell', 1949
# Command to update the book title
book.title = "Nineteen Eighty-Four"
book.save()
# Expected Output
# Changes saved to the database successfully
# Command to delete the book instance
book.delete()
# Expected Output
# (1, {'bookshelf.Book': 1})
