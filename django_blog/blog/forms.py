from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, Post
from taggit.forms import TagWidget

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # Email field (optional but useful)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
       
        
class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Enter comma-separated tags")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            "tags": TagWidget(),  # ✅ Add TagWidget for tag selection
            }  # Add TagWidget for tag selection

    def clean_tags(self):
        tags_str = self.cleaned_data['tags']
        return [tag.strip() for tag in tags_str.split(',')] if tags_str else []
