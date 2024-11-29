# relationship_app/views.py

from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect  # Used for rendering and redirection
from django.contrib.auth.views import LoginView, LogoutView  # Built-in views for authentication
from django.contrib.auth.forms import UserCreationForm  # Built-in form for user registration
from django.contrib.auth import login  # To log the user in after registration
from .models import Book, Library  # Import your models

# 1. Function-based view for listing books
def list_books(request):
    """
    Fetches all books from the database and renders them
    using the 'relationship_app/list_books.html' template.
    """
    books = Book.objects.all()  # Query all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# 2. Class-based view for library details
class LibraryDetailView(DetailView):
    """
    Displays details of a specific library.
    Uses the 'relationship_app/library_detail.html' template.
    """
    model = Library  # Specify the model for the view
    template_name = 'relationship_app/library_detail.html'  # Template to render
    context_object_name = 'library'  # The context variable for the template

# 3. Function-based view for user registration
def register(request):
    """
    Handles user registration using Django's built-in UserCreationForm.
    - If the form is valid, creates a new user and logs them in.
    - Redirects the user to the homepage after successful registration.
    """
    if request.method == 'POST':  # Check if the request is a POST request
        form = UserCreationForm(request.POST)  # Create a form instance with POST data
        if form.is_valid():  # Validate the form data
            user = form.save()  # Save the new user to the database
            login(request, user)  # Automatically log in the user
            return redirect('home')  # Redirect to the homepage or desired page
    else:
        form = UserCreationForm()  # Create an empty form for GET requests
    return render(request, 'register.html', {'form': form})

# 4. Class-based view for user login
class UserLoginView(LoginView):
    """
    Handles user login using Django's built-in LoginView.
    - Uses the 'login.html' template for rendering the login form.
    """
    template_name = 'login.html'  # Specify the template for login

# 5. Class-based view for user logout
class UserLogoutView(LogoutView):
    """
    Handles user logout using Django's built-in LogoutView.
    - Uses the 'logout.html' template to show a logout confirmation message.
    """
    template_name = 'logout.html'  # Specify the template for logout
