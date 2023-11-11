from django.shortcuts import render
from django.shortcuts import get_object_or_404
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
        # Fetch the user based on the authenticated user's username
        user = User.objects.get(username=request.user.username)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def delete(self, request, id):
        # Fetch the user based on the ID provided in the URL
        user = get_object_or_404(User, pk=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)