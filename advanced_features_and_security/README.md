# LibraryProject Permissions Setup

This Django app demonstrates managing permissions and groups.

## Custom Permissions Added
- `can_view`
- `can_create`
- `can_edit`
- `can_delete`

These are defined in the `Book` model inside `bookshelf/models.py`.

## User Groups
- **Viewers** → `can_view`
- **Editors** → `can_view`, `can_create`, `can_edit`
- **Admins** → All permissions

## Views and Permissions
The `book_list` view in `bookshelf/views.py` is protected using `@permission_required('bookshelf.can_view')`.

## Testing
1. Create users via the admin panel.
2. Assign them to groups.
3. Try accessing views to test permissions.

## Files Involved
- `models.py`: Custom permissions
- `views.py`: Protected views
- `README.md`: You're reading it 😉
