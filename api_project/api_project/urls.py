from django.contrib import admin
from django.urls import path, include
from api.views import BookViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookViewSet.as_view({'get': 'list'}), name='book-list'),
    path('api/', include('api.urls')),  # Include the api.urls module
]
