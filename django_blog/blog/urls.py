from django.urls import path  # For defining URL patterns
from django.contrib.auth.views import LoginView, LogoutView  # Built-in authentication views
from . import views  # Import views from the current app
from .views import (  # Import the class-based views for blog post management
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    add_comment,  # Import the add_comment view
    edit_comment,  # Import the edit_comment view
    delete_comment,  # Import the delete_comment view
)

# URL patterns for the blog app
urlpatterns = [
    # Authentication URLs
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),  # Login page
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),  # Logout page
    path('register/', views.register, name='register'),  # User registration
    path('profile/', views.profile, name='profile'),  # User profile

    # Blog Post Management URLs (CRUD)
    path('', PostListView.as_view(), name='post-list'),  # List all blog posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View details of a single post
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create a new post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Update an existing post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete a post

    # Comment Management URLs
    path('post/<int:post_id>/comments/new/', add_comment, name='add-comment'),  # Add a new comment
    path('comments/<int:comment_id>/edit/', edit_comment, name='edit-comment'),  # Edit an existing comment
    path('comments/<int:comment_id>/delete/', delete_comment, name='delete-comment'),  # Delete a comment
]


