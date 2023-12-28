from rest_framework import serializers
from .models import Notes
from django.core.validators import MinLengthValidator

class NoteSerializer(serializers.ModelSerializer):
    content = serializers.CharField(
        required=True,
        validators=[
            MinLengthValidator(15)
        ],
        max_length = 200
    )

    tags = serializers.ListField(
        child = serializers.CharField(
            max_length = 10
        ),
        required= False
    )
    class Meta:
        model = Notes
        fields = ['id', 'content', 'tags',]
        read_only_fields = ['id']

    # # Ensure that the 'user' field is required
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
