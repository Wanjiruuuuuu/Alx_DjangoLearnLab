# Create Operation

## Command
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

## Expected Output
```python
# Book object created successfully
# Book: 1984 by George Orwell (1949)
