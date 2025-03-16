from django.test import TestCase
from api.models import Book, Author

class BookAPITestCase(TestCase):
    def setUp(self):
        # Create an author instance first
        self.author = Author.objects.create(name="John Doe")

        # Now create book instances with a valid Author reference
        self.book1 = Book.objects.create(title="Django Basics", author=self.author, publication_year=2020)
        self.book2 = Book.objects.create(title="Advanced Django", author=self.author, publication_year=2022)

    def test_create_book(self):
        """Test creating a book"""
        new_book = Book.objects.create(title="REST API with Django", author=self.author, publication_year=2021)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(new_book.title, "REST API with Django")

    def test_get_book_list(self):
        """Test retrieving the list of books"""
        books = Book.objects.all()
        self.assertEqual(books.count(), 2)

    def test_filter_books(self):
        """Test filtering books by title"""
        books = Book.objects.filter(title="Django Basics")
        self.assertEqual(books.count(), 1)
        self.assertEqual(books.first().title, "Django Basics")

    def test_order_books(self):
        """Test ordering books by publication_year"""
        books = Book.objects.order_by("publication_year")
        self.assertEqual(books.first().title, "Django Basics")
        self.assertEqual(books.last().title, "Advanced Django")

    def test_search_books(self):
        """Test searching books by keyword"""
        books = Book.objects.filter(title__icontains="Django")
        self.assertEqual(books.count(), 2)

    def test_update_book(self):
        """Test updating a book"""
        self.book1.title = "Django for Beginners"
        self.book1.save()
        updated_book = Book.objects.get(id=self.book1.id)
        self.assertEqual(updated_book.title, "Django for Beginners")

    def test_delete_book(self):
        """Test deleting a book"""
        self.book1.delete()
        books = Book.objects.all()
        self.assertEqual(books.count(), 1)
