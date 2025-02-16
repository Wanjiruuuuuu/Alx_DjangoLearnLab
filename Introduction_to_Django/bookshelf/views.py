from django.shortcuts import render
from .models import Book

def home(request):
    """Home view that displays a list of all books"""
    books = Book.objects.all()
    return render(request, 'bookshelf/home.html', {'books': books})
