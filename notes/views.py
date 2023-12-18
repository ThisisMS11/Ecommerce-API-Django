from rest_framework import generics , permissions,status
from rest_framework.response import Response
from notes.models import Notes
from notes.serializers import CustomNotesSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class NotesViews(generics.CreateAPIView):
    model = Notes()
    serializer_class = CustomNotesSerializer

    # to define you can access this url.
    permission_classes = [
        permissions.IsAuthenticated
    ]

    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):
        # In your views.py, the line super().create(request, *args, **kwargs) is calling the create method of the superclass, which is generics.CreateAPIView. This is not related to the create method in serializers.py.
        super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_201_CREATED)
