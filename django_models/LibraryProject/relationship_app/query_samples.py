import os
import django
import sys

# Add project directory to Python path
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_path)

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    """Query all books by a specific author"""
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()
    except Author.DoesNotExist:
        return f"Author '{author_name}' not found"

def get_books_in_library(library_name):
    """List all books in a specific library"""
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return f"Library '{library_name}' not found"

def get_librarian_for_library(library_name):
    """Retrieve the librarian for a specific library"""
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except Library.DoesNotExist:
        return f"Library '{library_name}' not found"
    except Librarian.DoesNotExist:
        return f"No librarian found for library '{library_name}'"

# Example usage:
if __name__ == "__main__":
    # Create sample data
    author = Author.objects.create(name="J.K. Rowling")
    book1 = Book.objects.create(title="Harry Potter 1", author=author)
    book2 = Book.objects.create(title="Harry Potter 2", author=author)
    library = Library.objects.create(name="Fantasy Library")
    library.books.add(book1, book2)
    Librarian.objects.create(name="John Doe", library=library)

    # Test queries
    print("Books by J.K. Rowling:", get_books_by_author("J.K. Rowling"))
    print("Books in Fantasy Library:", get_books_in_library("Fantasy Library"))
    print("Librarian for Fantasy Library:", get_librarian_for_library("Fantasy Library"))
