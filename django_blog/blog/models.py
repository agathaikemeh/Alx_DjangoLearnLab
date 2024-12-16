from django.db import models  # Import Django's model utilities
from django.contrib.auth.models import User  # Import Django's built-in User model
from taggit.managers import TaggableManager  # Import TaggableManager for tagging

# Define the Post model
class Post(models.Model):
    # Title of the blog post
    title = models.CharField(max_length=200)
    # Content of the blog post
    content = models.TextField()
    # Timestamp for when the post is published
    published_date = models.DateTimeField(auto_now_add=True)
    # ForeignKey to associate the post with the author
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Tags to allow tagging of posts (many-to-many relationship managed by django-taggit)
    tags = TaggableManager()  # Adds tagging functionality to the Post model

    # String representation of the Post object
    def __str__(self):
        return self.title


# Define the Comment model
class Comment(models.Model):
    # ForeignKey to associate a comment with a specific post
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # ForeignKey to associate the comment with the user who wrote it
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Text field to store the content of the comment
    content = models.TextField()
    # Timestamp for when the comment was created
    created_at = models.DateTimeField(auto_now_add=True)
    # Timestamp for when the comment was last updated
    updated_at = models.DateTimeField(auto_now=True)

    # String representation of the Comment object
    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

