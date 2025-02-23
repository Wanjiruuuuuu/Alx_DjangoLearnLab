from django.contrib import admin
from django.urls import path
from relationship_app.views import list_authors

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', list_authors, name='list_authors'),
]
