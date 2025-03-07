from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Get all books from the database
    serializer_class = BookSerializer 
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing books.

    - Requires authentication (Token Authentication)
    - Supports CRUD operations: Create, Read, Update, Delete
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access
