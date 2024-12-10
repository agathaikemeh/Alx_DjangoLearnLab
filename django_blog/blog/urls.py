from django.urls import path  # Import the path function to define URL patterns
from django.contrib.auth.views import LoginView, LogoutView  # Import built-in views for login and logout
from .views import (  # Import class-based views for posts and comments
    PostListView,         # View to list all blog posts
    PostDetailView,       # View to display details of a single blog post
    PostCreateView,       # View to create a new blog post
    PostUpdateView,       # View to update an existing blog post
    PostDeleteView,       # View to delete a blog post
    CommentCreateView,    # View to create a new comment
    CommentUpdateView,    # View to update an existing comment
    CommentDeleteView,    # View to delete an existing comment
)

# URL patterns for the blog app
urlpatterns = [
    # ----------------------------------------
    # Authentication URLs
    # ----------------------------------------

    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    # Login page using Django's built-in LoginView and a custom template

    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    # Logout page using Django's built-in LogoutView and a custom template

    path('register/', PostListView.as_view(), name='register'),
    # Placeholder for the registration page (you may need to update this view)

    path('profile/', PostListView.as_view(), name='profile'),
    # Placeholder for the profile management page (you may need to update this view)

    # ----------------------------------------
    # Blog Post Management URLs (CRUD)
    # ----------------------------------------

    path('', PostListView.as_view(), name='post-list'),
    # List all blog posts at the root URL using PostListView

    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # View details of a single post using PostDetailView. <int:pk> captures the post ID.

    path('post/new/', PostCreateView.as_view(), name='post-create'),
    # Create a new post using PostCreateView

    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # Update an existing post using PostUpdateView. Restricted to the post's author.

    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # Delete an existing post using PostDeleteView. Restricted to the post's author.

    # ----------------------------------------
    # Comment Management URLs (CRUD)
    # ----------------------------------------

    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    # Add a new comment to a specific post using CommentCreateView.
    # <int:post_id> identifies the post to which the comment belongs.

    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    # Edit an existing comment using CommentUpdateView.
    # <int:pk> identifies the comment to be updated. Restricted to the comment's author.

    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    # Delete an existing comment using CommentDeleteView.
    # <int:pk> identifies the comment to be deleted. Restricted to the comment's author.
]



