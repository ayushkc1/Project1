from snippet.models import Snippet
from django.contrib.auth.models import User         
from snippet.serializers import SnippetSerializer , UserSerializer  
from rest_framework import viewsets
from rest_framework.response import Response

class SnippetViewSet(viewsets.ModelViewSet):   
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    def create(self, validiated_data):
        return Snippet.objects.create(**validiated_data)
 
    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
