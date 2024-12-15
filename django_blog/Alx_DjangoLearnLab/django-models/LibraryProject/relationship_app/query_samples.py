from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "Author Name"  # Replace with actual author name
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print("Books by the author:", books_by_author)

# List all books in a library
library_name = "Library Name"  # Replace with actual library name
library = Library.objects.get(name=library_name)  # Fetch the library by name
books_in_library = library.books.all()  # Get all books related to the library
print("Books in the library:", books_in_library)

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)  # Fetch librarian for the library
print("Librarian of the library:", librarian)


