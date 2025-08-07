# api/permissions.py

from rest_framework.permissions import BasePermission

class IsAdminOrEditor(BasePermission):
    """
    Custom permission to allow only users in 'Admins' or 'Editors' groups.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and (
                request.user.groups.filter(name="Admins").exists()
                or request.user.groups.filter(name="Editors").exists()
            )
        )
