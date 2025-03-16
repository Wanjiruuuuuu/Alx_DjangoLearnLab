from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class BookListView(generics.ListAPIView):
    """
    View to list all books in the system.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['title', 'author__name']  # `author__name` allows searching by author's name


class BookDetailView(generics.RetrieveAPIView):
    """
    View to retrieve a single book by its ID.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    search_fields = ['title', 'author__name']  # `author__name` allows searching by author's name
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering


class BookCreateView(generics.CreateAPIView):
    """
    View to create a new book.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

     # Filtering setup
    filterset_fields = ['title', 'author', 'publication_year']  # Allows filtering by these fields

class BookUpdateView(generics.UpdateAPIView):
    """
    View to update an existing book.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    View to delete a book.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

"""
Filtering, Searching, and Ordering:
 
Filtering: Use query parameters to filter by `title`, `author`, or `publication_year`.
   Example: `/api/books/?author=J.K. Rowling`

Searching: Use `search` to find books by title or author's name.
   Example: `/api/books/?search=Harry`

Ordering: Use `ordering` to sort books by `title` or `publication_year`.
   Example: `/api/books/?ordering=-publication_year`
"""
