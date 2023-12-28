from rest_framework import viewsets, status,permissions
from rest_framework.response import Response
from .models import Notes
from .serializers import NoteSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

class NoteViewSet(viewsets.ModelViewSet):

    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = [JWTAuthentication,SessionAuthentication,TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    # In Django REST Framework (DRF), the lookup_field attribute in a viewset is used to specify the field that should be used for looking up individual instances of the model when processing detail requests.
    lookup_field = 'id'


    def get_queryset(self):
        return Notes.objects.filter(user = self.request.user)

    def create(self, request, *args, **kwargs):
        # The get_serializer method is a part of the ModelViewSet and returns an instance of the serializer associated with the view.here NoteSerializer
        serializer = self.get_serializer(data=request.data)

        # Checks if the data provided to the serializer is valid
        serializer.is_valid(raise_exception=True)

        # Set the user of the new note to the currently authenticated user
        serializer.validated_data['user'] = self.request.user

        # Calls the perform_create method, which is a hook in the ModelViewSet that allows you to perform additional actions during the creation process.
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        print('serializer : \n', serializer,"\n");

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
