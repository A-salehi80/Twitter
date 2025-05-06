# serializers.py
from rest_framework import serializers
from .models import Post,Like


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'message', 'content', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'message', 'created_at', 'updated_at','on_post']
        read_only_fields = ['created_at', 'updated_at']

