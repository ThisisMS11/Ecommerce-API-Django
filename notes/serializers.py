from rest_framework import serializers
from notes.models import Notes
from django.core.validators import MinLengthValidator

class CustomNotesSerializer(serializers.ModelSerializer):
    content = serializers.CharField(
        required=True,
        validators=[
            MinLengthValidator(100)  
        ]
    )

    tags = serializers.ListField(
        child=serializers.CharField(max_length=50), 
        required=False
    )


    class Meta:
        model = Notes
        fields=(
            "content",
            "tags"
        )

    
    def create(self, validated_data):
        print(f"my new  user data  : {validated_data}")
        user = Notes.objects.create_user(
            username = validated_data['username'],
            email = validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()

        # here the returned user is the user's email 
        return user
    
