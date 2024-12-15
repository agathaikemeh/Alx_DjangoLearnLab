from django.shortcuts import render, redirect, get_object_or_404  # For rendering templates, redirecting, and retrieving objects
from django.contrib.auth.views import LoginView, LogoutView  # Built-in views for login and logout
from django.contrib.auth.decorators import login_required  # To restrict access to authenticated users
from django.contrib.auth.models import User  # The built-in User model
from django.http import HttpResponse  # For sending plain text responses
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView  # CBVs for CRUD
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # For permission control
from django.urls import reverse_lazy  # To redirect after deletion
from .forms import CustomUserCreationForm, CommentForm  # Import the custom registration form and CommentForm
from .models import Post, Comment  # Import Post and Comment models

# ----------------------------------------
# User Authentication Views
# ----------------------------------------

# View to handle user registration
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Bind data to the form
        if form.is_valid():  # Check if the form data is valid
            form.save()  # Save the user data to the database
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = CustomUserCreationForm()  # Create a blank form
    
    return render(request, 'blog/register.html', {'form': form})


# View to display and update the user's profile
@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user  # Get the currently logged-in user
        email = request.POST.get('email')  # Retrieve the 'email' field from the POST data
        if email:
            user.email = email  # Update the user's email address
            user.save()  # Save the updated user information
            return HttpResponse("Profile updated successfully!")
    return render(request, 'blog/profile.html', {'user': request.user})


# ----------------------------------------
# Blog Post Management Views (CRUD)
# ----------------------------------------

# View to list all blog posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']


# View to display details of a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


# View to create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# View to update an existing post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# View to delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# ----------------------------------------
# Comment Management Views (CRUD)
# ----------------------------------------

# Class-based view to create a comment
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the comment author
        form.instance.post = get_object_or_404(Post, id=self.kwargs['post_id'])  # Link the comment to the post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['post_id']})  # Redirect to the post detail page


# Class-based view to update a comment
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  # Ensure only the author can edit the comment

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.id})  # Redirect to the post detail page


# Class-based view to delete a comment
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  # Ensure only the author can delete the comment

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.id})  # Redirect to the post detail page



