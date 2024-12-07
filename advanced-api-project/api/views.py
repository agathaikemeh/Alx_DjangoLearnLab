from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, filters  # Import filters module
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

def root_view(request):
    """
    Root view for the API.
    """
    return HttpResponse("Welcome to the API!")

class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all books with filtering, searching, and ordering capabilities.

    - **URL**: GET /books/
    - **Permissions**: Public (no authentication required).
    - **Behavior**:
      - Queries all book records from the database.
      - Serializes the results using the `BookSerializer`.
      - Allows filtering by title, author, and publication year.
      - Allows searching by title and author.
      - Allows ordering by title and publication year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Add filter backends for filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields available for filtering
    filterset_fields = ['title', 'author', 'publication_year']

    # Fields available for search
    search_fields = ['title', 'author']

    # Fields available for ordering
    ordering_fields = ['title', 'publication_year']

    # Default ordering (optional)
    ordering = ['title']
