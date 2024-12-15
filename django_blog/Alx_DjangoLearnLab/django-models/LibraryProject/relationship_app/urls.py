from . import views  # Import the views module
from django.urls import path
from django.contrib.auth import views as auth_views  # Import Django's built-in authentication views
from .views import list_books, LibraryDetailView, register, home  # Import views including register

urlpatterns = [
    # Home URL
    path('', home, name='home'),  # Home page view

    # Book-related URLs
    path('books/', list_books, name='list_books'),  # URL for listing all books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for library detail

    # Authentication URLs
    path('login/', views.CustomLoginView.as_view(template_name='login.html'), name='login'),  # Login URL with template
    path('logout/', views.CustomLogoutView.as_view(template_name='logout.html'), name='logout'),  # Logout URL with template
    path('register/', views.register, name='register'),  # Register URL

    # Role-based URLs
    path('admin/', views.admin_view, name='admin_view'),  # Admin-only view
    path('librarian/', views.librarian_view, name='librarian_view'),  # Librarian-only view
    path('member/', views.member_view, name='member_view'),  # Member-only view
]

