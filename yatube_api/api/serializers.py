from rest_framework import serializers

from posts.models import Comment, Group, Post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    # Я так понимаю, что slug лучше.
    # Он подходит для полей модели с unique=True,
    # Что бы однозначно идентифицировать автора.
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Post
        fields = (
            'id', 'text', 'pub_date', 'author', 'image', 'group', 'comments'
        )
