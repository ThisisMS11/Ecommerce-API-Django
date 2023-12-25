from rest_framework import generics, permissions,status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from notes.models import Notes
from rest_framework.response import Response
from notes.serializers import CustomNotesSerializer , getNotesSerializer ,notesUpdateSerializer
from django.http import Http404
from django.shortcuts import get_object_or_404


# To create a note
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

# to list down all the notes 
class ListNotesView(generics.ListAPIView):
    serializer_class = getNotesSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user  # Access the current user
        return Notes.objects.filter(user=user)  # Filter notes for that user

# to delete a note 
class DeleteNoteViews(generics.DestroyAPIView):
    queryset = Notes.objects.all()
    authentication_classes = [JWTAuthentication, SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        """Handle the deletion and return a success response."""
        id = kwargs.get("id")
        note = Notes.objects.filter(id=id, user=self.request.user).first()

        if note is None:
            raise Http404("Note not found.")

        self.perform_destroy(note)
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class UpdateNoteViews(generics.UpdateAPIView):
    serializer_class = notesUpdateSerializer
    queryset = Notes.objects.all()
    authentication_classes = [JWTAuthentication, SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # this is to get the desired note using the id given.
    def get_object(self):
        note_id = self.kwargs.get('id')
        if note_id is None:
            raise Http404('Note not found')
        return get_object_or_404(self.queryset, id=note_id, user=self.request.user)

    # Handles GET requests to the update endpoint. Retrieves the existing note object, serializes it, and returns the serialized data as a response. This is used to pre-fill the DRF interface.
    def get(self, request, *args, **kwargs):
        # id = kwargs.get('id');
        # print('id  : ', id)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)



