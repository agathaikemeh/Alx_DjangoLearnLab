from django.contrib.auth.forms import UserCreationForm  # Import the built-in user creation form
from django.contrib.auth.models import User  # Import the built-in User model
from django import forms  # Import Django's forms module
from .models import Post, Comment  # Import the Post and Comment models for creating forms
from taggit.forms import TagField, TagWidget  # Import TagField and TagWidget from django-taggit

# -------------------------------------------------------
# User Registration Form
# -------------------------------------------------------

# Custom form extending the built-in UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    # Adding an email field to the default UserCreationForm
    email = forms.EmailField(required=True)  # Make the email field mandatory

    class Meta:
        # Specify the model and fields this form works with
        model = User  # The form is based on the built-in User model
        fields = ['username', 'email', 'password1', 'password2']  # Fields to display and process

    def save(self, commit=True):
        """
        Override the save method to handle the email field correctly.
        """
        user = super().save(commit=False)  # Get a User object without saving it
        user.email = self.cleaned_data['email']  # Set the email field

        if commit:
            user.save()  # Save the User object if commit=True
        return user


# -------------------------------------------------------
# Blog Post Form
# -------------------------------------------------------

class PostForm(forms.ModelForm):
    # Add a tags field using TagField with a custom TagWidget for better UI/UX
    tags = TagField(
        required=False,  # Tags are optional
        widget=TagWidget(attrs={
            'class': 'form-control',  # Bootstrap class for styling
            'placeholder': 'Add tags, separated by commas'  # Placeholder text
        })
    )

    class Meta:
        # Specify the model and fields this form works with
        model = Post
        fields = ['title', 'content', 'tags']  # Include the 'tags' field

        # Custom widgets for title and content fields
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title of your post'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your content here'
            }),
        }

    def save(self, commit=True, request=None):
        """
        Override the save method to handle tags and set the author of the post.
        """
        post = super().save(commit=False)  # Get a Post object without saving it

        # If a request object is passed, set the author as the logged-in user
        if request and hasattr(request, 'user'):
            post.author = request.user

        if commit:
            post.save()  # Save the Post object
            self.save_m2m()  # Save many-to-many relationships (tags)

        return post  # Return the saved Post object


# -------------------------------------------------------
# Comment Form
# -------------------------------------------------------

class CommentForm(forms.ModelForm):
    class Meta:
        # Specify the model and fields this form works with
        model = Comment
        fields = ['content']  # Only the content field is needed for comments

        # Custom widget for better UI/UX
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',  # Bootstrap class for styling
                'placeholder': 'Write your comment here...',  # Placeholder text
                'rows': 3,  # Height of the textarea
            }),
        }
