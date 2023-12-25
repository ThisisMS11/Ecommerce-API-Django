from rest_framework import serializers
from notes.models import Notes
from django.core.validators import MinLengthValidator

class CustomNotesSerializer(serializers.ModelSerializer):
    content = serializers.CharField(
        required=True,
        validators=[
            MinLengthValidator(15)  
        ]
    )

    tags = serializers.ListField(
        child=serializers.CharField(max_length=5), 
        required=True
    )

    class Meta:
        model = Notes
        fields = (
            "content",
            "tags"
        )
        
    def create(self, validated_data):
        tags = validated_data.pop('tags', [])  # Extract tags from validated_data
        instance = self.Meta.model.objects.create_note(tags=tags, **validated_data)
        return instance
