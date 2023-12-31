from django.contrib.auth import get_user_model
from rest_framework import generics , permissions,status
from rest_framework.response import Response
from users.serializers import CustomUserSerializer
# Create your views here.

class UserViews(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = CustomUserSerializer

    # to define you can access this url.
    permission_classes = [
        permissions.AllowAny
    ]

    def create(self, request, *args, **kwargs):
        # In your views.py, the line super().create(request, *args, **kwargs) is calling the create method of the superclass, which is generics.CreateAPIView. This is not related to the create method in serializers.py.
        super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_201_CREATED)
