# Import necessary models
from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(book.title)
    except Author.DoesNotExist:
        print(f"No author found with the name {author_name}")

# List all books in a specific library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Many-to-many relationship
        print(f"Books in {library_name} library:")
        for book in books:
            print(book.title)
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")

# Retrieve the librarian for a specific library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)  # One-to-one relationship
        print(f"The librarian for {library_name} library is {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for {library_name}")

# Example Usage
if __name__ == "__main__":
    # Query all books by a specific author
    books_by_author("J.K. Rowling")

    # List all books in a specific library
    books_in_library("Central Library")

    # Retrieve the librarian for a specific library
    librarian_for_library("Central Library")


