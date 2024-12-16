from django.urls import path
from django.contrib.auth import views as auth_views  # Import Django's built-in authentication views
from . import views  # Import the views module
from .views import (
    list_books,
    LibraryDetailView,
    register,
    home,
    admin_view,
    librarian_view,
    member_view,
)

urlpatterns = [
    # Home URL
    path('', home, name='home'),  # Home page view

    # Book-related URLs
    path('books/', list_books, name='list_books'),  # URL for listing all books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # URL for library detail

    # Authentication URLs
    path('login/', views.CustomLoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Login URL with template
    path('logout/', views.CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Logout URL with template
    path('register/', register, name='register'),  # Register URL

    # Role-based URLs
    path('admin-view/', admin_view, name='admin_view'),  # Admin-only view
    path('librarian-view/', librarian_view, name='librarian_view'),  # Librarian-only view
    path('member-view/', member_view, name='member_view'),  # Member-only view

    # Django authentication views (if using default login/logout)
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),  # Password reset view
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),  # Password reset done view
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # Password reset confirm view
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),  # Password reset complete view
]


