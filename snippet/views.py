from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from snippet.models import Snippet
from rest_framework.parsers import JSONParser           
from snippet.serializers import SnippetSerializer   

# Create your views here.
def snippet_list(request):
    if request.method=='GET':
        snippets=Snippet.objects.all()
        serializer=SnippetSerializer(snippets,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
    
def snippet_detail(request,pk):
    try:
        snippet=Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method=='GET':
        serializer=SnippetSerializer(snippet)
        return JsonResponse(serializer.data)
    
    elif request.method=='PUT':
        data=JSONParser().parse(request)
        serializer=SnippetSerializer(snippet,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)
    
    elif request.method=='DELETE':
        snippet.delete()
        return HttpResponse(status=204)
    