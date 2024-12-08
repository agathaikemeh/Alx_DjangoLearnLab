from django.shortcuts import render, redirect  # For rendering templates and redirecting users
from django.contrib.auth.views import LoginView, LogoutView  # Built-in views for login and logout
from django.contrib.auth.decorators import login_required  # To restrict access to authenticated users
from django.contrib.auth.models import User  # The built-in User model
from django.http import HttpResponse  # For sending plain text responses
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView  # CBVs for CRUD
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # For permission control
from django.urls import reverse_lazy  # To redirect after deletion
from .forms import CustomUserCreationForm  # Import the custom registration form
from .models import Post  # Import the Post model

# ----------------------------------------
# User Authentication Views
# ----------------------------------------

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


# ----------------------------------------
# Blog Post Management Views (CRUD)
# ----------------------------------------

# View to list all blog posts
class PostListView(ListView):
    model = Post  # Specify the model to fetch data
    template_name = 'blog/post_list.html'  # Specify the template file
    context_object_name = 'posts'  # Use 'posts' in the template to access data
    ordering = ['-published_date']  # Show newest posts first

# View to display details of a single post
class PostDetailView(DetailView):
    model = Post  # Specify the model to fetch data
    template_name = 'blog/post_detail.html'  # Specify the template file

# View to create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post  # Specify the model to save data
    fields = ['title', 'content']  # Fields to display in the form
    template_name = 'blog/post_form.html'  # Template for the form

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the logged-in user as the author
        return super().form_valid(form)  # Validate and save the form

# View to update an existing post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post  # Specify the model to update data
    fields = ['title', 'content']  # Fields to display in the form
    template_name = 'blog/post_form.html'  # Template for the form

    def form_valid(self, form):
        form.instance.author = self.request.user  # Ensure the logged-in user is the author
        return super().form_valid(form)  # Validate and save the form

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Allow only the post author to update

# View to delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post  # Specify the model to delete data
    template_name = 'blog/post_confirm_delete.html'  # Confirmation template
    success_url = reverse_lazy('post-list')  # Redirect to post list after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Allow only the post author to delete

