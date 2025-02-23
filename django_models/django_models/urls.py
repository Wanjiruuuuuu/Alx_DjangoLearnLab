from django.contrib import admin
from django.urls import path
from relationship_app.views import list_authors, list_books_in_library, retrieve_librarian_for_library
from relationship_app.views import list_authors

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', list_authors, name='list_authors'),
    path('libraries/<str:library_name>/books/', list_books_in_library, name='list_books_in_library'),
    path('libraries/<str:library_name>/librarian/', retrieve_librarian_for_library, name='retrieve_librarian_for_library'),
]
