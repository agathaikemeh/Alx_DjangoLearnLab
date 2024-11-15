from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "Author Name"  # Replace with an existing author name
books_by_author = Book.objects.filter(author__name=author_name)
print(f"Books by {author_name}:")
for book in books_by_author:
    print(book.title)

# List all books in a library
library_name = "Library Name"  # Replace with an existing library name
try:
    library = Library.objects.get(name=library_name)
    print(f"Books in {library_name}:")
    for book in library.books.all():
        print(book.title)
except Library.DoesNotExist:
    print("Library not found")

# Retrieve the librarian for a library
try:
    librarian = Librarian.objects.get(library__name=library_name)
    print(f"Librarian for {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print("Librarian not found")
