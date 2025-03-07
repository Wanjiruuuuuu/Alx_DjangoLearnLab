from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    
    path('', include(router.urls)),
    path('books/', BookList.as_view(), name='book-list'),
]
