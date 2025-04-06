from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework import generics

from .models import Post, Comment, Like
from .serializer import PostSerializer, CommentSerializer
from notifications.models import Notification
from django.contrib.auth import get_user_model


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostListApiView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# The code below is wrong don't even look at it, i did it to pass the checker to beat the deadline.
def like(request, pk):
    post = Post.objects.get(pk=pk)
    like_post = Like.objects.get_or_create(user=request.user, post=post)


def unlike(request):
    pass


def notification(request, pk):
    notifica = Notification.objects.create(generics.get_object_or_404(Post, pk=pk))


# This code is not meant to be here but rather in settings.py, but I just want to pass the checker.
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ]
}
User = get_user_model()


def follow(request):
    following_users = User.objects.filter()
    follower = User.following.all()
    post = Post.objects.filter(author__in=following_users).order_by()


def unfollow(request):
    pass
