from django.http import JsonResponse
from relationship_app.models import Author, Book, Library, Librarian
from relationship_app.query_samples import get_books_in_library, get_librarian_for_library

def list_authors(request):
    authors = Author.objects.all().values('id', 'name')
    return JsonResponse(list(authors), safe=False)

def list_books_in_library(request, library_name):
    books = get_books_in_library(library_name)
    return JsonResponse(list(books.values('id', 'title')), safe=False)
    return JsonResponse(list(books.values('id', 'title')), safe=False)

def retrieve_librarian_for_library(request, library_name):
    librarian = get_librarian_for_library(library_name)
    return JsonResponse({'id': librarian.id, 'name': librarian.name})
    return JsonResponse({'id': librarian.id, 'name': librarian.name})
