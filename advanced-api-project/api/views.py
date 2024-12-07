from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError
from .models import Book
from .serializers import BookSerializer

# View to list all books
class BookListView(generics.ListAPIView):
    """
    This view retrieves a list of all books in the database.

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
    This view retrieves the details of a specific book using its primary key.

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
    This view allows authenticated users to create a new book.

    - **URL**: POST /books/add/
    - **Permissions**: 
      - Authenticated users: Can create a new book.
      - Unauthenticated users: Read-only access.
    - **Behavior**:
      - Validates the data using the `BookSerializer`.
      - Creates a new book record if data is valid.
      - Raises a `ValidationError` if the data is invalid.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

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
    This view allows authenticated users to update an existing book.

    - **URL**: PUT /books/<int:pk>/edit/
    - **Permissions**: 
      - Authenticated users: Can update book details.
      - Unauthenticated users: Read-only access.
    - **Behavior**:
      - Validates the updated data using the `BookSerializer`.
      - Updates the book record if data is valid.
      - Raises a `ValidationError` if the data is invalid.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

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
    This view allows authenticated users to delete a book.

    - **URL**: DELETE /books/<int:pk>/delete/
    - **Permissions**: 
      - Authenticated users: Can delete a book.
      - Unauthenticated users: Read-only access.
    - **Behavior**:
      - Deletes the book record identified by its primary key (pk).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

