from rest_framework import viewsets, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from Relation.models import Relation
from .models import Post,Like
from .serializers import PostSerializer,LikeSerializer

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Post.objects.select_related('posted_by').all()
        # return Post.objects.select_related('posted_by').prefetch_related('posted_by__profile')

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)

class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Like.objects.select_related('liked_by').all()

    def perform_create(self, serializer):
        on_post=serializer.validated_data['on_post']
        existing = Like.objects.filter(liked_by=self.request.user,on_post=on_post)
        if existing.exists():
            raise ValidationError('This post is already liked')
        serializer.save(liked_by=self.request.user)

class FollowingPostsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get users the current user is following
        following_users = Relation.objects.filter(follower=request.user).values_list('following_id', flat=True)
        # Get posts from those users
        posts = Post.objects.filter(posted_by__in=following_users).select_related('posted_by')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


