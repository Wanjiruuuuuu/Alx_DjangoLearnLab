from django.shortcuts import render, redirect
from django.contrib.auth import login, logout # Handles user login and logouts
from django.contrib.auth.forms import AuthenticationForm  #Built in login forms
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from taggit.models import Tag
from django.db.models import Q



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

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return self.object.post.get_absolute_url()


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return self.object.post.get_absolute_url()
    


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            post.tags.set(form.cleaned_data['tags'])  # Assign tags
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


def search_posts(request):
    query = request.GET.get("q")
    results = []
    
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)
        ).distinct()

    return render(request, 'blog/search_results.html', {'results': results, 'query': query})

def posts_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = Post.objects.filter(tags=tag)
    return render(request, "blog/posts_by_tag.html", {"tag": tag, "posts": posts})

class PostByTagListView:
    model = Post
    template_name = "blog/post_list.html" 
    context_object_name = "posts"

    def get_queryset(self):
        tag = get_object_or_404(Tag, slug=self.kwargs.get("tag_slug"))
        return Post.objects.filter(tags__in=[tag])
