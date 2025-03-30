from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from rest_framework.views import APIView  # Importing the missing APIView
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated  # Importing the missing IsAuthenticated
from .permissions import IsOwnerOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    """
    Viewset for handling CRUD operations on posts.
    Users can only edit or delete their own posts.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    Viewset for handling CRUD operations on comments.
    Users can only edit or delete their own comments.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        following_users = user.profile.following.all()  # Assuming a `following` field in the profile
        posts = Post.objects.filter(author__in=following_users).order_by("-created_at")
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if created:
        # Create notification
        Notification.objects.create(
            recipient=post.user,
            actor=request.user,
            verb="liked",
            target_content_type=ContentType.objects.get_for_model(post),
            target_object_id=post.pk
        )
        return JsonResponse({"message": "Post liked!"}, status=201)

    return JsonResponse({"message": "Already liked."}, status=400)

@login_required
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like = Like.objects.filter(user=request.user, post=post)

    if like.exists():
        like.delete()
        return JsonResponse({"message": "Post unliked!"}, status=200)

    return JsonResponse({"message": "You haven't liked this post."}, status=400)
