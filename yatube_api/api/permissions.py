from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Не автор не может изменять или удалять пост."""

    def has_object_permission(self, request, view, obj):
        #  Разрешает метод GET для не автора
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
