from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

# View to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/list_books.html', {'books': books})

# View to create a new book
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        publication_year = request.POST['publication_year']
        Book.objects.create(title=title, author=author, publication_year=publication_year)
        return redirect('list_books')
    return render(request, 'bookshelf/create_book.html')

# View to edit an existing book
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.publication_year = request.POST['publication_year']
        book.save()
        return redirect('list_books')
    return render(request, 'bookshelf/edit_book.html', {'book': book})

# View to delete a book
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('list_books')
