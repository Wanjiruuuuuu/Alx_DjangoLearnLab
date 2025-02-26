from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import list_books
from .views import LibraryDetailView
from . import views
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
    path("admin/", admin_view, name="admin_view"),
    path("librarian/", librarian_view, name="librarian_view"),
    path("member/", member_view, name="member_view"),
]
