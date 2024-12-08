from django.contrib.auth.forms import UserCreationForm  # Import the built-in user creation form
from django.contrib.auth.models import User  # Import the built-in User model
from django import forms  # Import Django's forms module

# Custom form extending the built-in UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    # Adding an email field to the default UserCreationForm
    email = forms.EmailField(required=True)

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
