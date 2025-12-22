from rest_framework import serializers
from users.models import User
from django.db import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_name', 'email', 'date_joined']
    

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)  # Hide in output, validate length

    class Meta:
        model = User
        fields = ['user_name', 'email', 'password']

    def create(self, validated_data):
        """
        Create and return a new `Register` instance, given the validated data.
        """
        user = User.objects.create_user(
            email=validated_data['email'],
            user_name=validated_data['user_name'],
            password=validated_data['password'],
        )

        return user


class LoginSerializer(serializers.Serializer):
    email       = serializers.EmailField()
    password    = serializers.CharField(write_only=True, min_length=8) 