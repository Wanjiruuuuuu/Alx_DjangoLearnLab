from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

# Query all libraries that have a specific book
def get_libraries_with_book(book_title):
    book = Book.objects.get(title=book_title)
    return Library.objects.filter(books=book)

# Query all librarians in a specific library
def get_librarians_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.filter(library=library)
