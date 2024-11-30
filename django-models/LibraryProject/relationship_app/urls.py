from django.urls import path
from django.contrib.auth import views as auth_views  # Import Django's built-in authentication views
from .views import list_books, LibraryDetailView, register, home  # Import the correct views

urlpatterns = [
    # Home URL
    path('', home, name='home'),  # Home page view

    # Book-related URLs
    path('books/', list_books, name='list_books'),  # URL for listing all books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for library detail

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Login URL
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),  # Logout URL
    path('register/', register, name='register'),  # Register URL (function-based)
]

