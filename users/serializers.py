# users/serializers.py
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from . import models

# class UserCreateSerializer(UserCreateSerializer):
#     class Meta(UserCreateSerializer.Meta):
#         model = models.User
#         fields = '__all__'
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('id', 'email', 'username')
        exclude = ('password', 'current_password')

        
    def create(self, validated_data):
        user = models.User.objects.create_user(**validated_data)
        return user
    
 