from django.test import TestCase
from relationship_app.models import Author, Book, Library, Librarian
from relationship_app.query_samples import get_books_by_author, get_books_in_library, get_librarian_for_library

class AuthorModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")

    def test_author_creation(self):
        self.assertEqual(self.author.name, "Test Author")

class BookModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(title="Test Book", author=self.author)

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author.name, "Test Author")

class LibraryModelTest(TestCase):
    def setUp(self):
        self.library = Library.objects.create(name="Test Library")

    def test_library_creation(self):
        self.assertEqual(self.library.name, "Test Library")

class LibrarianModelTest(TestCase):
    def setUp(self):
        self.library = Library.objects.create(name="Test Library")
        self.librarian = Librarian.objects.create(name="Test Librarian", library=self.library)

    def test_librarian_creation(self):
        self.assertEqual(self.librarian.name, "Test Librarian")
        self.assertEqual(self.librarian.library.name, "Test Library")

class QuerySamplesTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.book1 = Book.objects.create(title="Test Book 1", author=self.author)
        self.book2 = Book.objects.create(title="Test Book 2", author=self.author)
        self.library = Library.objects.create(name="Test Library")
        self.library.books.add(self.book1, self.book2)
        self.librarian = Librarian.objects.create(name="Test Librarian", library=self.library)

    def test_get_books_by_author(self):
        books = get_books_by_author("Test Author")
        self.assertEqual(len(books), 2)

    def test_get_books_in_library(self):
        books = get_books_in_library("Test Library")
        self.assertEqual(len(books), 2)

    def test_get_librarian_for_library(self):
        librarian = get_librarian_for_library("Test Library")
        self.assertEqual(librarian.name, "Test Librarian")
