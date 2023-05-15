from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from django.http import JsonResponse
from rest_framework.response import Response

#using function Viewset
# class StudentViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Student.objects.all()
#         # serializer = StudentSerializer(queryset)
#         # print(serializer.data)
#         # for data in queryset:
#         #     print(data.name)
#         return Response(list(queryset.values()))

#     # queryset = Student.objects.all()
#     # serializer_class = StudentSerializer
    
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    