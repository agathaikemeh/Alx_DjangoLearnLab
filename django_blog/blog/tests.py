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
    # Tagging Tests
    # ----------------------------------------

    def test_tags_saved_on_post_creation(self):
        """
        Test that tags are saved correctly when a post is created.
        """
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('post-create'), {
            'title': 'New Post with Tags',
            'content': 'This post has tags.',
            'tags': 'tag1, tag2, tag3',
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful creation
        post = Post.objects.get(title="New Post with Tags")
        self.assertEqual(list(post.tags.names()), ['tag1', 'tag2', 'tag3'])

    def test_filter_posts_by_tag(self):
        """
        Test filtering posts by a specific tag.
        """
        response = self.client.get(reverse('tagged-posts', args=['django']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "First Post")
        self.assertNotContains(response, "Second Post")

    # ----------------------------------------
    # Search Functionality Tests
    # ----------------------------------------

    def test_search_by_title(self):
        """
        Test that posts can be searched by title.
        """
        response = self.client.get(reverse('search-posts'), {'q': 'First'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "First Post")
        self.assertNotContains(response, "Second Post")

    def test_search_by_content(self):
        """
        Test that posts can be searched by content.
        """
        response = self.client.get(reverse('search-posts'), {'q': 'second post'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Second Post")
        self.assertNotContains(response, "First Post")

    def test_search_by_tag(self):
        """
        Test that posts can be searched by tag.
        """
        response = self.client.get(reverse('search-posts'), {'q': 'tutorial'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Second Post")
        self.assertNotContains(response, "First Post")

    def test_search_no_results(self):
        """
        Test that a search query with no matches returns an empty result.
        """
        response = self.client.get(reverse('search-posts'), {'q': 'nonexistent'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No results found")  # Update this to match your search template

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



