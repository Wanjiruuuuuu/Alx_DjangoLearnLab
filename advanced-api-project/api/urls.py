from django.contrib import admin
from django.urls import path
from api.views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, home_redirect

urlpatterns = [
    path('', home_redirect), 
    path('admin/', admin.site.urls),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/create/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]
