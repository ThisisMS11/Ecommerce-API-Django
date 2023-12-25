from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from notes.models import Notes
from notes.serializers import CustomNotesSerializer

class NotesViews(generics.CreateAPIView):
    serializer_class = CustomNotesSerializer

    authentication_classes = [JWTAuthentication, SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CustomNotesSerializer
        return CustomNotesSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
