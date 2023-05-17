from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello World")

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .serializers import UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserProfileSerializer
from .models import UserProfile
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        role = request.data.get('role')

        user = authenticate(username=username, password=password)
        if user and user.userprofile.role == role:
            login(request, user)
            serializer = UserProfileSerializer(user.userprofile)
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#
class UserAPIView(APIView):
    def get(self, request):
        users = UserProfile.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return Response(serializer.data)
class UserAPIViewSingle(APIView):
    def get(self, request,pk):
        users = UserProfile.objects.get(pk=pk)
        serializer = UserProfileSerializer(users)
        return Response(serializer.data)
