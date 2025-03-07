from django.contrib import admin
from django.urls import path, include
from api.views import BookList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookList.as_view(), name='book-list'),
    path('api/', include('api.urls')),  # Include the api.urls module
]
