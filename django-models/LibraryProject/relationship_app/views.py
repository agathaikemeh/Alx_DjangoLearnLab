from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test  # Decorator to restrict access based on user role
from .models import Book, Library, UserProfile  # Import UserProfile for role-based checking

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
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')  # Redirect to the homepage or desired page
    else:
        form = UserCreationForm()  # Create an empty form for GET requests
    return render(request, 'registration/register.html', {'form': form})

# 4. Class-based view for user login
class CustomLoginView(LoginView):
    """
    Handles user login using Django's built-in LoginView.
    - Uses the 'login.html' template for rendering the login form.
    """
    template_name = 'login.html'  # Specify the template for login

# 5. Class-based view for user logout
class CustomLogoutView(LogoutView):
    """
    Handles user logout using Django's built-in LogoutView.
    - Uses the 'logout.html' template to show a logout confirmation message.
    """
    template_name = 'logout.html'  # Specify the template for logout
    next_page = 'login'  # Redirect to login page after logout

# 6. Simple home view for redirection
def home(request):
    """
    A simple home page view.
    """
    return HttpResponse("Welcome to the Home Page!")

# 7. Admin view: Only accessible to users with 'Admin' role
@user_passes_test(lambda u: u.userprofile.role == 'Admin', login_url='login')
def admin_view(request):
    """
    Admin-only view.
    """
    return render(request, 'admin_view.html')

# 8. Librarian view: Only accessible to users with 'Librarian' role
@user_passes_test(lambda u: u.userprofile.role == 'Librarian', login_url='login')
def librarian_view(request):
    """
    Librarian-only view.
    """
    return render(request, 'librarian_view.html')

# 9. Member view: Only accessible to users with 'Member' role
@user_passes_test(lambda u: u.userprofile.role == 'Member', login_url='login')
def member_view(request):
    """
    Member-only view.
    """
    return render(request, 'member_view.html')


