from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile

class UserRoleTestCase(TestCase):
    
    def setUp(self):
        """
        This method runs before each test. It creates test users and associates user profiles with roles.
        """
        # Creating test users
        self.admin_user = User.objects.create_user(username='adminuser', password='password123')
        self.librarian_user = User.objects.create_user(username='librarianuser', password='password123')
        self.member_user = User.objects.create_user(username='memberuser', password='password123')

        # Creating corresponding UserProfile entries
        UserProfile.objects.create(user=self.admin_user, role='Admin')
        UserProfile.objects.create(user=self.librarian_user, role='Librarian')
        UserProfile.objects.create(user=self.member_user, role='Member')

        # URLs to test
        self.admin_url = reverse('admin_view')
        self.librarian_url = reverse('librarian_view')
        self.member_url = reverse('member_view')

    def test_admin_view_access(self):
        """
        Test that only Admin users can access the admin_view.
        """
        # Log in as admin
        self.client.login(username='adminuser', password='password123')
        response = self.client.get(self.admin_url)
        self.assertEqual(response.status_code, 200)  # Should be able to access

        # Log in as librarian
        self.client.login(username='librarianuser', password='password123')
        response = self.client.get(self.admin_url)
        self.assertEqual(response.status_code, 302)  # Should be redirected (not authorized)

        # Log in as member
        self.client.login(username='memberuser', password='password123')
        response = self.client.get(self.admin_url)
        self.assertEqual(response.status_code, 302)  # Should be redirected (not authorized)

    def test_librarian_view_access(self):
        """
        Test that only Librarian users can access the librarian_view.
        """
        # Log in as librarian
        self.client.login(username='librarianuser', password='password123')
        response = self.client.get(self.librarian_url)
        self.assertEqual(response.status_code, 200)  # Should be able to access

        # Log in as admin
        self.client.login(username='adminuser', password='password123')
        response = self.client.get(self.librarian_url)
        self.assertEqual(response.status_code, 302)  # Should be redirected (not authorized)

        # Log in as member
        self.client.login(username='memberuser', password='password123')
        response = self.client.get(self.librarian_url)
        self.assertEqual(response.status_code, 302)  # Should be redirected (not authorized)

    def test_member_view_access(self):
        """
        Test that only Member users can access the member_view.
        """
        # Log in as member
        self.client.login(username='memberuser', password='password123')
        response = self.client.get(self.member_url)
        self.assertEqual(response.status_code, 200)  # Should be able to access

        # Log in as admin
        self.client.login(username='adminuser', password='password123')
        response = self.client.get(self.member_url)
        self.assertEqual(response.status_code, 302)  # Should be redirected (not authorized)

        # Log in as librarian
        self.client.login(username='librarianuser', password='password123')
        response = self.client.get(self.member_url)
        self.assertEqual(response.status_code, 302)  # Should be redirected (not authorized)

    def test_user_registration(self):
        """
        Test user registration functionality.
        """
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'password123',
            'password2': 'password123',
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after successful registration
        new_user = User.objects.get(username='newuser')
        self.assertIsNotNone(new_user)  # New user should be created

    def test_user_login(self):
        """
        Test the login functionality.
        """
        # Test login for admin user
        response = self.client.post(reverse('login'), {
            'username': 'adminuser',
            'password': 'password123',
        })
        self.assertEqual(response.status_code, 302)  # Should redirect (successful login)
        self.assertContains(response, 'Welcome')

        # Test login for non-existing user
        response = self.client.post(reverse('login'), {
            'username': 'nonexistinguser',
            'password': 'password123',
        })
        self.assertEqual(response.status_code, 200)  # Should remain on login page (unsuccessful login)

    def test_user_logout(self):
        """
        Test the logout functionality.
        """
        self.client.login(username='adminuser', password='password123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)  # Should log out and display logout page
        self.assertNotIn('_auth_user_id', self.client.cookies)  # Should not be logged in anymore

