from django.core.exceptions import ValidationError
from rest_framework import viewsets, permissions
from .models import Relation
from .serializers import RelationSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status

class RelationViewSet(viewsets.ModelViewSet):
    serializer_class = RelationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Relation.objects.all()

    def get_queryset(self):
        return Relation.objects.select_related('follower', 'following').filter(follower=self.request.user)

    def perform_create(self, serializer):
        following = serializer.validated_data['following']
        follower = self.request.user

        if Relation.objects.filter(follower=follower, following=following).exists():
            raise ValidationError("You are already following this user.")

        if follower == following:
            raise ValidationError("You cannot follow yourself.")

        serializer.save(follower=follower)
    def destroy(self, request, *args, **kwargs):
        relation = self.get_object()
        if relation.follower != request.user:
            raise PermissionDenied("You can only unfollow users you are following.")
        relation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


