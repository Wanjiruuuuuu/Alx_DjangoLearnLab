from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import list_books
from .views import LibraryDetailView
from .views import LibraryDetailView  # Ensure LibraryDetailView is imported
from . import views

urlpatterns = [
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Add URL pattern for LibraryDetailView
]
from .views import add_book, edit_book, delete_book
from .views import admin_view, librarian_view, member_view
from .views import admin_view, librarian_view, member_view


urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path(
        "login/",
        LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="registration/login.html"),
        name="logout",
    ),
    path("register/", views.register, name="register"),
    # Removed duplicate entries
    path("admin/", admin_view, name="admin_view"),
    path("librarian/", librarian_view, name="librarian_view"),
    path("member/", member_view, name="member_view"),
    path("add_book/", add_book, name="add_book"), 
    path("edit_book/<int:book_id>/", edit_book, name="edit_book"),
    path("delete_book/<int:book_id>/", delete_book, name="delete_book"),
    # Removed duplicate entries
]
