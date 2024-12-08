
from django.contrib.auth.forms import UserCreationForm  # Import the built-in user creation form
from django.contrib.auth.models import User  # Import the built-in User model
from django import forms  # Import Django's forms module
from .models import Post  # Import the Post model for creating and updating blog posts


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
    class Meta:
        # Specify the model and fields this form works with
        model = Post  # The form is based on the Post model
        fields = ['title', 'content']  # Fields to display and process in the form

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

        # If commit is True, save the Post object to the database
        if commit:
            post.save()

        # Return the Post object
        return post
