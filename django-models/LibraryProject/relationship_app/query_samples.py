from relationship_app.models import Author, Book

def query_books_by_author(author_name):
    try:
        # Get the Author object with the specified name
        author = Author.objects.get(name=author_name)

        # Filter and return books written by the specific author
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        print("Author not found.")
        return None

