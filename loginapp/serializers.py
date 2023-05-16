from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    role = serializers.CharField(max_length=20)
    class Meta:
        model = UserProfile
        fields = ['user','role']
