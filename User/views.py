from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from .models import User
from .utils import get_tokens_for_user
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import viewsets,permissions
from .permissions import IsOwner
class SignInView(APIView):
    def post(self, request):
        phone = request.data.get("phone")
        password = request.data.get("password")

        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            tokens = get_tokens_for_user(user)
            serializer = UserSerializer(user)
            return Response({
                "user": serializer.data,
                "tokens": tokens
            }, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class SignUpView(APIView):
    def post(self, request):
        required_fields = ["phone", "password"]
        for field in required_fields:
            if not request.data.get(field):
                return Response({field: "This field is required."}, status=status.HTTP_400_BAD_REQUEST)

        phone = request.data["phone"]
        password = request.data["password"]

        if User.objects.filter(phone=phone).exists():
            return Response({"phone": "A user with this phone number already exists."},
                            status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            phone=phone,
            password=password,
        )
        tokens = get_tokens_for_user(user)
        serializer = UserSerializer(user)
        return Response({
            "user": serializer.data,
            "tokens": tokens
        }, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("You do not have permission to access this profile.")
        return obj
