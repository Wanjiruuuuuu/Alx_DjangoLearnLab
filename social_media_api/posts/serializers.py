from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'  # Include all fields in the Post model

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'  # Include all fields in the Comment model
