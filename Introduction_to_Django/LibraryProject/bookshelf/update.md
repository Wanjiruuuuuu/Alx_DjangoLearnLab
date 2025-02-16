# Update Operation

## Command
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
```

## Expected Output
```python
# Book title updated successfully
# Updated Book: Nineteen Eighty-Four by George Orwell (1949)
