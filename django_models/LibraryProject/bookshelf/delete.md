# Delete Operation

## Command
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
```

## Expected Output
```python
# Book deleted successfully
# Attempting to retrieve the book again:
# Book matching query does not exist.
