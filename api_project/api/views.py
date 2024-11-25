from rest_framework import viewsets  # Import for ModelViewSet
from rest_framework import generics  # Import for generic views
from rest_framework.permissions import IsAuthenticated  # Import permission class
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    """
    API view to retrieve a list of books.
    Only authenticated users can access this view.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Apply IsAuthenticated permission

# Define the BookViewSet class
class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Book instances.
    Only authenticated users can access this API.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Apply IsAuthenticated permission
