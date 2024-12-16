from django.contrib.auth.forms import UserCreationForm  # Import the built-in user creation form
from django.contrib.auth.models import User  # Import the built-in User model
from django import forms  # Import Django's forms module
from .models import Post, Comment  # Import the Post and Comment models for creating forms
from taggit.forms import TagField, TagWidget  # Import TagField and TagWidget from django-taggit

# -------------------------------------------------------
# User Registration Form
# -------------------------------------------------------

class CustomUserCreationForm(UserCreationForm):
    """
    Custom form extending the built-in UserCreationForm to include an email field.
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        """
        Override the save method to include the email field.
        """
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# -------------------------------------------------------
# Blog Post Form
# -------------------------------------------------------

class PostForm(forms.ModelForm):
    """
    Form for creating and updating blog posts with a custom tags field.
    """
    tags = TagField(
        required=False,  # Tags are optional
        widget=TagWidget(attrs={  # Use TagWidget for better tag input UI
            'class': 'form-control',  # Apply Bootstrap styling
            'placeholder': 'Add tags, separated by commas',  # Placeholder for the input
        })
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include the 'tags' field
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title of your post',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your content here',
            }),
        }

    def save(self, commit=True, request=None):
        """
        Override the save method to handle tags and set the author of the post.
        """
        post = super().save(commit=False)  # Get a Post instance without saving
        if request and hasattr(request, 'user'):
            post.author = request.user  # Set the author to the logged-in user
        if commit:
            post.save()  # Save the Post instance
            self.save_m2m()  # Save many-to-many relationships (tags)
        return post


# -------------------------------------------------------
# Comment Form
# -------------------------------------------------------

class CommentForm(forms.ModelForm):
    """
    Form for creating and updating comments.
    """
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your comment here...',
                'rows': 3,
            }),
        }

