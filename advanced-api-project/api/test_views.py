from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Book, Author
from django.urls import reverse  

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="John Doe")

        self.book1 = Book.objects.create(title="Django Basics", author=self.author, publication_year=2020)
        self.book2 = Book.objects.create(title="Advanced Django", author=self.author, publication_year=2022)

        self.book_list_url = reverse('book-list')  

    def test_create_book(self):
        """Test creating a book via API and check response data"""
        data = {"title": "REST API with Django", "author": self.author.id, "publication_year": 2021}
        response = self.client.post(self.book_list_url, data, format='json')
        
        # Assertions
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("title", response.data)
        self.assertEqual(response.data["title"], "REST API with Django")

    def test_get_book_list(self):
        """Test retrieving the list of books and ensure response data is returned"""
        response = self.client.get(self.book_list_url)
        
        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)  # Ensure response is a list
        self.assertGreaterEqual(len(response.data), 2)  # At least 2 books

    def test_filter_books(self):
        """Test filtering books by title and check response"""
        response = self.client.get(self.book_list_url, {"title": "Django Basics"})
        
        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Django Basics")

    def test_update_book(self):
        """Test updating a book and check response"""
        book_url = reverse('book-detail', kwargs={'pk': self.book1.id})  
        updated_data = {"title": "Django for Beginners", "author": self.author.id, "publication_year": 2020}
        
        response = self.client.put(book_url, updated_data, format='json')

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Django for Beginners")

    def test_delete_book(self):
        """Test deleting a book and check response"""
        book_url = reverse('book-detail', kwargs={'pk': self.book1.id})  
        
        response = self.client.delete(book_url)

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

