from rest_framework import serializers
from users.models import User
from django.core.validators import MinLengthValidator
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators=[
            MinLengthValidator(10)  # Replace 5 with the minimum length you want
        ]
    )
    
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset= User.objects.all()
            )
        ]
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[
            validate_password
        ],
        style={
            "input_type":"password"
        }
    )

    password2 = serializers.CharField(
        write_only=True,
        validators=[
            validate_password
        ],
        style={
            "input_type":"password"
        }
    )

    class Meta:
        model = User
        fields=(
            "username",
            "email",
            "password",
            "password2"
        )

    # write down custom functions to check input validity
    def validate(self,attrs):
        if attrs["password"]!=attrs["password2"]:
            raise serializers.ValidationError({
                "password":"Password fields didn't match"
            })
        return attrs
    
    def create(self, validated_data):
        print(f"my new  user data  : {validated_data}")
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()

        # here the returned user is the user's email 
        return user
    
