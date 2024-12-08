from django.shortcuts import render, redirect  # For rendering templates and redirecting users
from django.contrib.auth.views import LoginView, LogoutView  # Built-in views for login and logout
from django.contrib.auth.decorators import login_required  # To restrict access to authenticated users
from django.contrib.auth.models import User  # The built-in User model
from django.http import HttpResponse  # For sending plain text responses
from .forms import CustomUserCreationForm  # Import the custom registration form

# View to handle user registration
def register(request):
    # If the request method is POST, process the form data
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Bind data to the form
        if form.is_valid():  # Check if the form data is valid
            form.save()  # Save the user data to the database
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        # If the request method is GET, create a blank form
        form = CustomUserCreationForm()
    
    # Render the registration template and pass the form to it
    return render(request, 'blog/register.html', {'form': form})


# View to display and update the user's profile
@login_required  # Ensures only authenticated users can access this view
def profile(request):
    # Check if the request is a POST request (indicating form submission)
    if request.method == 'POST':
        user = request.user  # Get the currently logged-in user
        email = request.POST.get('email')  # Retrieve the 'email' field from the POST data

        # If an email is provided in the form data
        if email:
            user.email = email  # Update the user's email address
            user.save()  # Save the updated user information to the database

            # Return a simple success message
            return HttpResponse("Profile updated successfully!")

    # If the request is not POST, render the profile page with the current user data
    return render(request, 'blog/profile.html', {'user': request.user})

