from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile

class RoleBasedAccessTests(TestCase):

    def setUp(self):
        # Clear existing UserProfiles to avoid UNIQUE constraint issues
        UserProfile.objects.all().delete()

        self.admin_user = User.objects.create_user(username='admin', password='password')
        self.librarian_user = User.objects.create_user(username='librarian', password='password')
        self.member_user = User.objects.create_user(username='member', password='password')

        # Create UserProfile
        # Clear existing UserProfiles to avoid UNIQUE constraint issues
        UserProfile.objects.all().delete()
        
        UserProfile.objects.create(user=self.admin_user, role='Admin')
        UserProfile.objects.create(user=self.librarian_user, role='Librarian')
        UserProfile.objects.create(user=self.member_user, role='Member')

    def test_admin_view_access(self):
        self.client.login(username='admin', password='password')
        response = self.client.get(reverse('admin_view'))
        self.assertEqual(response.status_code, 200)

    def test_librarian_view_access(self):
        self.client.login(username='librarian', password='password')
        response = self.client.get(reverse('librarian_view'))
        self.assertEqual(response.status_code, 200)

    def test_member_view_access(self):
        self.client.login(username='member', password='password')
        response = self.client.get(reverse('member_view'))
        self.assertEqual(response.status_code, 200)

    def test_admin_view_access_denied_for_librarian(self):
        # Log in the librarian user
        # Log in the librarian user
        # Log in the librarian user
        self.client.login(username='librarian', password='password')
        response = self.client.get(reverse('admin_view'))
        self.assertEqual(response.status_code, 403)

    def test_admin_view_access_denied_for_member(self):
        # Log in the member user
        # Log in the member user
        # Log in the member user
        self.client.login(username='member', password='password')
        response = self.client.get(reverse('admin_view'))
        self.assertEqual(response.status_code, 403)

    def test_librarian_view_access_denied_for_member(self):
        # Log in the member user
        # Log in the member user
        # Log in the member user
        self.client.login(username='member', password='password')
        response = self.client.get(reverse('librarian_view'))
        self.assertEqual(response.status_code, 403)
