# Library Project

## Permissions and Groups Setup

This project implements a permission and group management system to control access to various parts of the application.

### Custom Permissions
The following custom permissions have been added to the `Book` model:
- `can_view`: Permission to view book instances.
- `can_create`: Permission to create new book instances.
- `can_edit`: Permission to edit existing book instances.
- `can_delete`: Permission to delete book instances.

### User Groups
The following groups can be created in the Django admin interface:
- **Editors**: Assigned permissions to create and edit books (`can_create`, `can_edit`).
- **Viewers**: Assigned permission to view books (`can_view`).
- **Admins**: Assigned all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`).

### Enforcing Permissions
Permissions are enforced in the views using the `@permission_required` decorator. For example:
```python
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # View logic here
```

### Testing
To test the implementation:
1. Create test users and assign them to the appropriate groups.
2. Log in as these users and attempt to access various parts of the application to ensure that permissions are applied correctly.

### Conclusion
This setup enhances the security and functionality of the application by controlling access based on user roles and their assigned permissions.
