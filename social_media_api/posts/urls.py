from django.urls import path
from .views import FeedView

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
    path('<int:pk>/like/', like_post, name='like_post'),
    path('<int:pk>/unlike/', unlike_post, name='unlike_post'),
]
