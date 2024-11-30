from . import views  # Import the views module
from django.urls import path
from django.contrib.auth import views as auth_views  # Import Django's built-in authentication views
from .views import list_books, LibraryDetailView, register, home  # Import the register view

urlpatterns = [
    # Home URL
    path('', home, name='home'),  # Home page view

    # Book-related URLs
    path('books/', list_books, name='list_books'),  # URL for listing all books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for library detail

    # Authentication URLs
    path('login/', views.CustomLoginView.as_view(), name='login'),  # Login URL
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),  # Logout URL
    path('register/', views.register, name='register'),  # Register URL
]


