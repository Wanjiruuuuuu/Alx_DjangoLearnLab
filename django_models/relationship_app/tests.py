from django.test import TestCase
from relationship_app.models import Author, Book, Library, Librarian

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
