from django.http import JsonResponse
from relationship_app.models import Author

def list_authors(request):
    authors = Author.objects.all().values('id', 'name')
    return JsonResponse(list(authors), safe=False)
