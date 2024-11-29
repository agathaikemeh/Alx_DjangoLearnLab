# relationship_app/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views  # Import Django's built-in authentication views
from .views import list_books, LibraryDetailView, register  # Import the views

urlpatterns = [
    # URL for listing all books
    path('books/', list_books, name='list_books'),

    # URL for library detail
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', register, name='register'),
]

