from rest_framework.routers import DefaultRouter
from rest_framework.urls import urlpatterns
from django.urls import path
from .views import FollowingPostsView, PostViewSet, LikeViewSet

app_name='Relation'
router = DefaultRouter()
router.register(r'Posts', PostViewSet, basename='Posts')
router.register(r'Likes', LikeViewSet, basename='Likes'
                )
urlpatterns += [
    path('following-posts/', FollowingPostsView.as_view(), name='following-posts'),
]
urlpatterns += router.urls