from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test, login_required

from .models import Book, Library  # Importing Library model
from .models import Library  # Ensure Library model is imported

# Create your views here.
from django.contrib.auth.decorators import permission_required

@permission_required('relationship_app.can_add_book')
def add_book(request):
    # Logic for adding a book
    pass

@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    # Logic for editing a book
    pass

@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    # Logic for deleting a book
    pass

def list_books(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "relationship_app/list_books.html", context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Add books to context
        return context

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Your account has been created, you can login.")
            return redirect("/relationship_app/login")
    else:
        form = UserCreationForm()
    context = {"form": form}
    return render(request, "relationship_app/register.html", context)

def LoginView(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, "registration/register.html")
    else:
        return render(request, "details not matching")

def LogoutView(request):
    logout(request)
    return render(request, "registration/logout.html")

# Role-based views
@login_required
@user_passes_test(lambda u: u.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@login_required
@user_passes_test(lambda u: u.userprofile.role == 'Librarian')
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@login_required
@user_passes_test(lambda u: u.userprofile.role == 'Member')
def member_view(request):
    return render(request, "relationship_app/member_view.html")
