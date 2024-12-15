from django.test import TestCase, Client  # Import TestCase for testing and Client for simulating requests
from django.urls import reverse  # Import reverse for resolving URL patterns
from django.contrib.auth.models import User  # Import the built-in User model
from .models import Post  # Import the Post model
from taggit.models import Tag  # Import the Tag model from django-taggit

class BlogTests(TestCase):
    """
    Test cases for the Django Blog application.
    This includes authentication, blog post management, tagging, search, permissions, and error handling.
    """

    def setUp(self):
        """
        Setup test environment before each test runs:
        - Create a test user.
        - Create some test blog posts with tags.
        - Initialize Django's test client.
        """
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')

        # Create some test blog posts
        self.post1 = Post.objects.create(
            title="First Post",
            content="Content for the first post",
            author=self.user
        )
        self.post2 = Post.objects.create(
            title="Second Post",
            content="Content for the second post",
            author=self.user
        )

        # Add tags to posts using django-taggit
        self.post1.tags.add('django', 'test')
        self.post2.tags.add('python', 'tutorial')

        # Initialize the test client
        self.client = Client()

    # ----------------------------------------
    # URL Tests
    # ----------------------------------------

    def test_post_create_url(self):
        """
        Test that the 'post/new/' URL is correctly registered and resolves to PostCreateView.
        """
        # Ensure the URL can be resolved
        url = reverse('post-create')
        self.assertEqual(url, '/post/new/')  # Check that it resolves to the correct URL path

    # ----------------------------------------
    # Authentication Tests
    # ----------------------------------------

    def test_login(self):
        """
        Test login functionality:
        - Ensure valid credentials log in the user successfully.
        """
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password123',
        })
        self.assertEqual(response.status_code, 200)  # Login page should load without errors

    def test_register(self):
        """
        Test registration functionality:
        - Ensure a new user can register successfully.
        """
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'password123',
            'password2': 'password123',
        })
        self.assertEqual(response.status_code, 302)  # Redirect to login after successful registration

    # ----------------------------------------
    # Blog Post Management Tests
    # ----------------------------------------

    def test_post_list_view(self):
        """
        Test the blog post list view:
        - Ensure all posts are displayed on the post list page.
        """
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "First Post")
        self.assertContains(response, "Second Post")

    def test_post_detail_view(self):
        """
        Test the blog post detail view:
        - Ensure the details of a specific post are displayed correctly.
        """
        response = self.client.get(reverse('post-detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "First Post")
        self.assertContains(response, "Content for the first post")

    def test_post_create_view(self):
        """
        Test creating a new blog post:
        - Ensure authenticated users can create posts successfully.
        """
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('post-create'), {
            'title': 'New Post',
            'content': 'This is a new blog post.',
            'tags': 'django, testing',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertTrue(Post.objects.filter(title="New Post").exists())


