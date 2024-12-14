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

    # Overriding the save method to include the email field
    def save(self, commit=True):
        # Call the parent class's save method to get a User object without saving it to the database yet
        user = super().save(commit=False)

        # Add the email field's data to the User object
        user.email = self.cleaned_data['email']

        # If commit is True, save the User object to the database
        if commit:
            user.save()
        
        # Return the User object
        return user


# -------------------------------------------------------
# Blog Post Form
# -------------------------------------------------------

# Custom form for creating and updating blog posts
class PostForm(forms.ModelForm):
    # Add a tags field to allow users to input tags for their posts
    tags = TagField(
        required=False,
        widget=TagWidget(attrs={
            'class': 'form-control', 
            'placeholder': 'Add tags, separated by commas'
        })
    )

    class Meta:
        # Specify the model and fields this form works with
        model = Post  # The form is based on the Post model
        fields = ['title', 'content', 'tags']  # Include the 'tags' field

        # Add custom widgets for better styling and user experience
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

    # Overriding the save method to set the author of the post
    def save(self, commit=True, request=None):
        # Call the parent class's save method to get a Post object without saving it to the database yet
        post = super().save(commit=False)

        # If a request object is provided, set the author to the logged-in user
        if request and hasattr(request, 'user'):
            post.author = request.user

        # Save the post instance
        if commit:
            post.save()

        # Save the tags separately after the post object has been saved
        self.save_m2m()

        # Return the Post object
        return post


# -------------------------------------------------------
# Comment Form
# -------------------------------------------------------

# Custom form for creating and updating comments
class CommentForm(forms.ModelForm):
    class Meta:
        # Specify the model and fields this form works with
        model = Comment  # The form is based on the Comment model
        fields = ['content']  # Fields to display and process in the form

        # Add custom widgets for better styling and user experience
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',  # Bootstrap class for styling
                'placeholder': 'Write your comment here...',  # Placeholder text
                'rows': 3,  # Height of the textarea
            }),
        }

