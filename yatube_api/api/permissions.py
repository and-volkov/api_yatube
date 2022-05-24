from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Не автор не может изменять или удалять запись."""
    def has_object_permission(self, request, view, obj):
        # кроме такого варианта не придумал как их объединить.
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
