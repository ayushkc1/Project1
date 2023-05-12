from rest_framework import serializers

class StudentSerializer(serializers.Serializer):   #Serializer class with base class serializers.Serializer) that is inherited
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)