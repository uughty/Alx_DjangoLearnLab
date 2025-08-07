from rest_framework.permissions import BasePermission

class IsAdminOrEditor(BasePermission):
    """
    Custom permission to allow only Admins or Editors to access.
    """
    def has_permission(self, request, view):
        return request.user and (
            request.user.groups.filter(name='Admins').exists() or
            request.user.groups.filter(name='Editors').exists()
        )
