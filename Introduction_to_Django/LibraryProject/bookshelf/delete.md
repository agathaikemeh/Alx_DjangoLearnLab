# Delete Operation

## Command:
```python
from bookshelf.models import Book

# Retrieving the book instance to delete
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Verify deletion by fetching all books
books = Book.objects.all()
print(books)
<QuerySet []>
