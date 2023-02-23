from django.contrib.auth import get_user_model
from rest_framework import serializers
import django.contrib.auth.password_validation as validators
from datetime import datetime

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'last_login',
            'first_name',
            'last_name',
            'role'
        ]

class CustomRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'role',
            'password',
        ]
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        # print(validated_data)
        user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                fullName=validated_data['fullName'],
                password=validated_data['password'],
                last_login = datetime.now())
        return user

    def validate_password(self, data):
        validators.validate_password(password=data, user=get_user_model())
        return data