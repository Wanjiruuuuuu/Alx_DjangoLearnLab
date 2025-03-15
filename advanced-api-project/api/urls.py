from django.contrib import admin
from django.urls import path
from api.views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, home_redirect

urlpatterns = [
    path('', home_redirect), 
    path('admin/', admin.site.urls),
    path('books/', BookListView.as_view(), name='book/list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book/detail'),
    path('books/create/', BookCreateView.as_view(), name='book/create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book/update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book/delete'),
]
