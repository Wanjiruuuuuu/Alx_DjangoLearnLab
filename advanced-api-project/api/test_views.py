from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Book, Author

class BookTests(APITestCase):
    def setUp(self):
        """Create test user, author, and book"""
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")  # ✅ Ensure login
        
        self.author = Author.objects.create(name="Test Author")
        self.book1 = Book.objects.create(title="Django Basics", author=self.author, publication_year=2020)
    
    def test_get_books(self):
        """Test retrieving books"""
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        """Test creating a new book"""
        data = {
            "title": "New Book",
            "author": self.author.id,
            "publication_year": 2022
        }
        response = self.client.post("/api/books/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

    def test_update_book(self):
        """Test updating a book"""
        update_url = f"/api/books/{self.book1.id}/"
        updated_data = {
            "title": "Updated Django Basics",
            "author": self.author.id,
            "publication_year": 2021
        }
        response = self.client.put(update_url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Django Basics")

    def test_delete_book(self):
        """Test deleting a book"""
        delete_url = f"/api/books/{self.book1.id}/"
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

