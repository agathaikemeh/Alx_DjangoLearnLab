from django.contrib import admin  # Import Django's admin utilities
from .models import Post, Comment  # Import your custom models

# ----------------------------------------
# Admin Customization for Post Model
# ----------------------------------------

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Post model.
    - Displays specific fields in the list view.
    - Adds search and filter functionality.
    """
    list_display = ('title', 'author', 'published_date')  # Columns to display in the admin list view
    list_filter = ('published_date', 'author', 'tags')  # Filters for the sidebar
    search_fields = ('title', 'content')  # Enables search by title and content
    ordering = ('-published_date',)  # Orders posts by most recent first

# ----------------------------------------
# Admin Customization for Comment Model
# ----------------------------------------

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Comment model.
    - Displays relevant comment fields in the list view.
    - Adds filters and search functionality for comments.
    """
    list_display = ('author', 'post', 'created_at', 'updated_at')  # Columns to display
    list_filter = ('created_at', 'author')  # Filters for the sidebar
    search_fields = ('content', 'author__username')  # Enables search by content and author username
    ordering = ('-created_at',)  # Orders comments by most recent first
