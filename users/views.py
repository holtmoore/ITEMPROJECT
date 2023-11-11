from django.shortcuts import render
from users.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny


# Create your views here.
class UserDetail(APIView):
    def get(self, request):
        user = User.objects.get(username=request.user.username)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def delete(self, request):
        user = User.objects.get(username=request.user.username)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
