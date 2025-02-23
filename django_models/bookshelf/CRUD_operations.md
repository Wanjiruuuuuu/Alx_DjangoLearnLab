# CRUD Operations Documentation

## Create Operation
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```
Output: Book object created successfully

## Retrieve Operation  
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
```
Output: Title: 1984, Author: George Orwell, Year: 1949

## Update Operation
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
```
Output: Book title updated successfully

## Delete Operation
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
```
Output: Book deleted successfully

## Admin Interface Features
The Book model is registered in the Django admin interface with the following customizations:
- List display: title, author, publication_year
- List filters: publication_year, author
- Search fields: title, author
- Ordering: title
- Items per page: 20

To access the admin interface:
1. Create a superuser: `python manage.py createsuperuser`
2. Visit http://127.0.0.1:8000/admin/
3. Log in with your superuser credentials
