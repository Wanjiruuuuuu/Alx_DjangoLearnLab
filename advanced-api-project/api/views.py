from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class BookListView(generics.ListAPIView):
    """
    View to list all books in the system.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveAPIView):
    """
    View to retrieve a single book by its ID.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    View to create a new book.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

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
