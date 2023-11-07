from django.contrib.auth import get_user_model
from rest_framework import generics , permissions,status
from rest_framework.response import Response
from users.serializers import CustomUserSerializer
# Create your views here.

class UserViews(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = CustomUserSerializer

    permission_classes = [
        permissions.AllowAny
    ]

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_201_CREATED)
