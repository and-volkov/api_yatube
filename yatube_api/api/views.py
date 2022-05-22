from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from posts.models import Group, Comment, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вью-сет для модели групп."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Вью-сет для модели комментариев."""

    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        # Получает комментарии к отдельному посту.
        post_id = self.kwargs.get('post_id')
        queryset = Comment.objects.filter(post=post_id)
        return queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        serializer.save(
            author=self.request.user,
            post_id=post_id
        )


class PostViewSet(viewsets.ModelViewSet):
    """Вью-сет для модели постов."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        # Добавляет автора при создании поста
        serializer.save(author=self.request.user)
