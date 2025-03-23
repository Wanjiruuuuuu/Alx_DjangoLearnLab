from django.shortcuts import render, redirect
from django.contrib.auth import login, logout # Handles user login and logouts
from django.contrib.auth.forms import AuthenticationForm  #Built in login forms
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

@login_required
def profile(request):
    return render(request, 'blog/profile.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # Bind form with user data
        if form.is_valid():  # Validate form fields
            User = form.save() # save user to the database
            login(request, User) #automatically login the user
        return render(request, "blog/register.html")
    
    else:
        
        form = UserRegisterForm() # Create an empty form
    
    return render(request, 'users/register.html', {'form': form}) # Render the registration form with the given template


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  
    context_object_name = 'posts'
    ordering = ['-published_date']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    # ordering = ['-published_date']

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    context_object_name = 'post'
    # ordering = ['-published_date']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'


    def form_valid(self, form):
        return super().form_valid(form)
    
  
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Allow only authors to edit posts

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'    

    def test_func(self):
        Post == self.get_object()
        return super().test_func() # Allow only authors to delete

