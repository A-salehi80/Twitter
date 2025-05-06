from rest_framework import serializers
from .models import User, Profile


class ProfileSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio', 'followers', 'following']

    def get_followers(self, obj):
        # Get users who follow this user
        relations = obj.user.follower.select_related('follower')
        users = [relation.follower for relation in relations]
        return UserSerializer(users, many=True).data

    def get_following(self, obj):
        # Get users this user is following
        relations = obj.user.following.select_related('following')
        users = [relation.following for relation in relations]
        return UserSerializer(users, many=True).data

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['phone']
