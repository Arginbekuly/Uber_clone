#Django imports
from rest_framework.permissions import BasePermission, SAFE_METHODS


# Custom permission classes for account management
class IsAdminUser(BasePermission):
    """
    Allows access only to administrators.
    """

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.role == "admin"
        )


class IsOwner(BasePermission):
    """
    Access only if the user is working with their profile.
    """

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id


class IsAdminOrOwner(BasePermission):
    """
    Access if the user is the resource owner or administrator.
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.user.role == "admin"
            or obj.id == request.user.id
        )

class BanManagementPermission(BasePermission):
    """
    Allows only admins to perform certain actions.
    For example: banning/unbanning users.
    """
    allowed_admin_actions = {"ban", "unban"}

    def has_permission(self, request, view):
        if hasattr(view, 'action'):
            if view.action in self.allowed_admin_actions:
                return bool(request.user.is_authenticated and request.user.is_staff)
        return True