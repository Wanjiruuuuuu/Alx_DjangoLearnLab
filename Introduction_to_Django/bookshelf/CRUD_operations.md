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
