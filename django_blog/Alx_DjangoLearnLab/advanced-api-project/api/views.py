from django.shortcuts import render
from django.http import HttpResponse
from django_filters import rest_framework
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter, OrderingFilter  # Import necessary filters for search and ordering
from django_filters.rest_framework import DjangoFilterBackend  # Import DjangoFilterBackend for filtering
from .models import Book
from .serializers import BookSerializer

def root_view(request):
    return HttpResponse("Welcome to the API!")

# View to list all books with filtering, searching, and ordering capabilities
class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all books in the database with filtering, searching, and ordering.

    - **URL**: GET /books/
    - **Permissions**: Public (no authentication required).
    - **Behavior**:
      - Queries all book records from the database.
      - Serializes the results using the `BookSerializer`.
      - Allows filtering by title, author, and publication year.
      - Allows searching by title and author.
      - Allows ordering by title and publication year.
    """
    queryset = Book.objects.all()  # Retrieve all Book records from the database
    serializer_class = BookSerializer  # Use the BookSerializer to convert queryset to JSON

    # Specify the filter backends (for filtering, searching, and ordering)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    # Define the fields that can be used for filtering
    filterset_fields = ['title', 'author', 'publication_year']  # Users can filter by these fields

    # Specify the fields that can be searched (will search across title and author)
    search_fields = ['title', 'author']  # Users can search by title and author

    # Define the fields that users can order by
    ordering_fields = ['title', 'publication_year']  # Users can order by title and publication year

    # Set default ordering (optional)
    ordering = ['title']  # Default ordering will be by title if no specific ordering is provided

