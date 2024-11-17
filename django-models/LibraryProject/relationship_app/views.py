from django.views.generic.detail import DetailView
# relationship_app/views.py
from django.shortcuts import render
from .models import Book  # Import the Book model

def list_books(request):  # Define a function-based view called 'list_books'
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# relationship_app/views.py
from django.views.generic import DetailView
from .models import Library  # Import the Library model

class LibraryDetailView(DetailView):  # Create a class-based view for library details
    model = Library  # Specify the model as Library
    template_name = 'relationship_app/library_detail.html'  # Use this template to render the view
    context_object_name = 'library'  # Set the context variable to 'library'

