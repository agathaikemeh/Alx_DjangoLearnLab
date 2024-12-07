from django.shortcuts import render
from django.http import HttpResponse
# Import necessary classes and modules from Django REST Framework
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import ValidationError
from .models import Book
from .serializers import BookSerializer

def root_view(request):
    return HttpResponse("Welcome to the API!")

# View to list all books
class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all books in the database.

    - **URL**: GET /books/
    - **Permissions**: Public (no authentication required).
    - **Behavior**:
      - Queries all book records from the database.
      - Serializes the results using the `BookSerializer`.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# View to retrieve the details of a single book
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves the details of a specific book using its primary key.

    - **URL**: GET /books/<int:pk>/
    - **Permissions**: Public (no authentication required).
    - **Behavior**:
      - Looks up a book in the database by its primary key (pk).
      - Serializes the book's data using the `BookSerializer`.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# View to create a new book
class BookCreateView(generics.CreateAPIView):
    """
    Allows authenticated users to create a new book.

    - **URL**: POST /books/add/
    - **Permissions**: Only authenticated users can create books.
    - **Behavior**:
      - Validates the data using the `BookSerializer`.
      - Creates a new book record if data is valid.
      - Raises a `ValidationError` if the data is invalid.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Custom behavior for saving a new book.
        Ensures validation before saving to the database.
        """
        if serializer.is_valid():
            serializer.save()
        else:
            raise ValidationError("Invalid data submitted.")


# View to update an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    Allows authenticated users to update an existing book.

    - **URL**: PUT /books/<int:pk>/edit/
    - **Permissions**: Only authenticated users can update books.
    - **Behavior**:
      - Validates the updated data using the `BookSerializer`.
      - Updates the book record if data is valid.
      - Raises a `ValidationError` if the data is invalid.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        """
        Custom behavior for updating a book.
        Ensures validation before applying updates.
        """
        if serializer.is_valid():
            serializer.save()
        else:
            raise ValidationError("Update failed due to invalid data.")


# View to delete a book
class BookDeleteView(generics.DestroyAPIView):
    """
    Allows authenticated users to delete a book.

    - **URL**: DELETE /books/<int:pk>/delete/
    - **Permissions**: Only authenticated users can delete books.
    - **Behavior**:
      - Deletes the book record identified by its primary key (pk).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

