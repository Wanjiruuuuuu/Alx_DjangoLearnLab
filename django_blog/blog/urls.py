
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from blog import views
from .views import PostListView  # Import the view you want as home
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from .views import search_posts, posts_by_tag
from .views import(
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,

)

urlpatterns = [
   
    path('', PostListView.as_view(), name='home'),  # This sets 'home' as the main page
    path('posts/', PostListView.as_view(), name='posts'),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="blog/logout.html"), name="logout"),
    
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    path('search/', search_posts, name='search_posts'),
    path('tags/<slug:tag_slug>/', posts_by_tag, name='posts_by_tag'),

    path("search/", search_posts, name="search")

]

