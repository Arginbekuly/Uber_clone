from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminUser(BasePermission):
    """
    Разрешает доступ только администраторам.
    """

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.role == "admin"
        )


class IsOwner(BasePermission):
    """
    Доступ только если пользователь работает со своим профилем.
    """

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id


class IsAdminOrOwner(BasePermission):
    """
    Доступ если пользователь — владелец ресурса или администратор.
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.user.role == "admin"
            or obj.id == request.user.id
        )
