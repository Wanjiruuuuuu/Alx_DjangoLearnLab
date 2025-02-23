from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import list_books
from .views import LibraryDetailView
from . import views


urlpatterns = [
    path("", list_books, name="list_books"),
    path("library/<pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path(
        "relationship_app/login",
        LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "relationship_app/logout/",
        LogoutView.as_view(template_name="registration/login.html"),
        name="logout",
    ),
    path("relationship_app/register/", views.register, name="register"),
]
