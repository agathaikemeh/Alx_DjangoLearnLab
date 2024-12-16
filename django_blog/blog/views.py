from django.shortcuts import render, redirect, get_object_or_404  # Utilities for rendering and retrieving objects
from django.contrib.auth.views import LoginView, LogoutView  # Built-in authentication views
from django.contrib.auth.decorators import login_required  # Restrict access to logged-in users
from django.contrib.auth.models import User  # The built-in User model
from django.http import HttpResponse  # For sending plain HTTP responses
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView  # Class-based views for CRUD
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # Mixins for access control
from django.urls import reverse_lazy  # Utility for lazy URL reversing
from django.db.models import Q  # For advanced query lookups
from taggit.models import Tag  # Import Tag model from django-taggit
from .forms import CustomUserCreationForm, CommentForm  # Import custom forms
from .models import Post, Comment  # Import models for posts and comments

# ----------------------------------------
# User Authentication Views
# ----------------------------------------

def register(request):
    """
    View to handle user registration.
    - Displays a form for registration and processes user creation on submission.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    """
    View to display and update the user's profile.
    - Allows logged-in users to update their email.
    """
    if request.method == 'POST':
        user = request.user
        email = request.POST.get('email')  # Retrieve email from the form
        if email:
            user.email = email  # Update the user's email
            user.save()  # Save changes to the database
            return HttpResponse("Profile updated successfully!")
    return render(request, 'blog/profile.html', {'user': request.user})

# ----------------------------------------
# Blog Post Management Views (CRUD)
# ----------------------------------------

class PostListView(ListView):
    """ View to list all blog posts. """
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']  # Display posts in descending order of published date

class PostDetailView(DetailView):
    """ View to display a single blog post with its details. """
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    """ View to create a new blog post. """
    model = Post
    fields = ['title', 'content', 'tags']  # Include tags in the form
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the post author to the logged-in user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ View to update an existing blog post. """
    model = Post
    fields = ['title', 'content', 'tags']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Ensure the post remains associated with the logged-in user
        return super().form_valid(form)

    def test_func(self):
        """ Restrict access to the post's author only. """
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ View to delete a blog post. """
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        """ Restrict deletion access to the post's author only. """
        post = self.get_object()
        return self.request.user == post.author

# ----------------------------------------
# Tagging and Search Functionality
# ----------------------------------------

class TagPostListView(ListView):
    """
    View to display all blog posts filtered by a specific tag.
    - Retrieves posts associated with the tag provided in the URL.
    """
    model = Post
    template_name = 'blog/tag_post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """
        Fetch the tag from the URL and retrieve associated posts.
        - Uses `get_object_or_404` for proper error handling.
        """
        tag = get_object_or_404(Tag, name=self.kwargs.get('tag'))  # Get tag from the URL
        return Post.objects.filter(tags__name__in=[tag])  # Filter posts by tag

    def get_context_data(self, **kwargs):
        """
        Add the tag name to the context for use in the template.
        """
        context = super().get_context_data(**kwargs)
        context['tag'] = self.kwargs.get('tag')  # Include the tag name in the context
        return context

def search_posts(request):
    """
    View to handle search queries for blog posts.
    - Filters posts based on title, content, or tags.
    """
    query = request.GET.get('q')  # Retrieve the search term from the request
    results = Post.objects.none()  # Default to no results

    if query:
        # Filter posts that match the query in title, content, or tags
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()  # Remove duplicate results

    return render(request, 'blog/search_results.html', {'results': results, 'query': query})

# ----------------------------------------
# Comment Management Views (CRUD)
# ----------------------------------------

class CommentCreateView(LoginRequiredMixin, CreateView):
    """ View to create a new comment on a blog post. """
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the comment's author to the logged-in user
        form.instance.post = get_object_or_404(Post, id=self.kwargs['post_id'])  # Link comment to post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['post_id']})  # Redirect to post details

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ View to update an existing comment. """
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        """ Restrict update access to the comment's author only. """
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.id})  # Redirect to post details

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ View to delete an existing comment. """
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        """ Restrict delete access to the comment's author only. """
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.id})  # Redirect to post details




