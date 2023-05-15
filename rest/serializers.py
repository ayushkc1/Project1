from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest.models import Student
from . import models

class StudentSerializer(serializers.Serializer):  #Serializer class with base class serializers.Serializer) that is inherited
    id=serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    class Meta:
        model=Student
        fields=['id','name','roll','city'] #esle check matra garni ho
   
        
    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    
  