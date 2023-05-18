from snippet.models import Snippet
from rest_framework import serializers
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
   # owner = serializers.ReadOnlyField(source='owner.username')
    #The untyped ReadOnlyField is always read-only, and will be used for serialized representations, but will not be used for updating model instances when they are deserialized.

    
    class Meta:
        model = Snippet
        fields = '__all__'
        
    def create(self,validated_data):
        return Snippet.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.code=validated_data.get('code',instance.code)
        instance.linenos=validated_data.get('linenos',instance.linenos)
        instance.language=validated_data.get('language',instance.language)
        instance.style=validated_data.get('style',instance.style)
        instance.save()
        return instance
    
class UserSerializer(serializers.ModelSerializer):
   # snippets=serializers.PrimaryKeyRelatedField(many=True,queryset=Snippet.objects.all())
    class Meta:
        model=User
        fields=['id','username']