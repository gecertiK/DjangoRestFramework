from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Comment, Post


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'posts', 'comments']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    text = serializers.CharField(required=True)
    author = serializers.CharField(read_only=True)

    class Meta:
        model = Comment
        fields = ['url', 'id', 'created', 'text', 'author', 'post']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    author = serializers.CharField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['url', 'id', 'created', 'title', 'description', 'author', 'comments']
