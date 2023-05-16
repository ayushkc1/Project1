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
   
        
    def create(self,validated_data): #create method is used to create new object
        return Student.objects.create(**validated_data)
    
    def update(self,instance,validated_data):  #instance has old value and validated_data has new value
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance


#  from rest.models import Student
#  from rest_framework.renderers import JSONRenderer
#  from rest.serializers import StudentSerializer
#  from rest_framework.parsers import JSONParser
#  snippet=Student(name="shellmahi",roll=3,city="Butwal")
#  snippet.save()
# serializer = SnippetSerializer(snippet)
# serializer.data
# content = JSONRenderer().render(serializer.data)
# content