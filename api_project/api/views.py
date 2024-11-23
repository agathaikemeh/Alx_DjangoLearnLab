from rest_framework import viewsets  # Correct import for viewsets
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
#To Update the file by defining the BookViewSet class
class BookViewSet(viewsets.ModelViewSet):  # Used viewsets.ModelViewSet here
    queryset = Book.objects.all()
    serializer_class = BookSerializer