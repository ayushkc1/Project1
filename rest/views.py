from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



def student_details(request, pk):
    stu = Student.objects.get(id=pk)
    print(stu)  # object
    serializer = StudentSerializer(stu)
    print(serializer)  # object with its models
    print(serializer.data)  # data in dictionary format
    # converts data into json format
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data, content_type='application/json')


def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu,many=True)
    # converts data into json format
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')