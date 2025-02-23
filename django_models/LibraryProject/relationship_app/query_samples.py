from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author.
author_name = Author.objects.create("Robinson")
Author.objects.get(name=author_name)
author = Author.objects.get(id=1)
Book.objects.filter(author=author)


# List all books in a library.
library_name = Library.objects.create(name="Science")
library1 = Library.objects.get(name=library_name)
library1.books.all()

# Retrieve the librarian for a library.

Librarian.objects.get(library=library1)
