from rest_framework.decorators import api_view
from rest_framework.response import Response
from restpractise.models import Company,Employee
from .serializers import CompanySerializer,EmployeeSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# @api_view(['GET'])
# def getData(request):
#     items=Item.objects.all()
#     serializer=ItemSerializer(items,many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def addItem(request):
#     serializer=ItemSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
        
#     return Response(serializer.data)

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class= CompanySerializer
    
    
    #companies/{companyId}/employees
    # detail set True because primary key must be passed compulsorily
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        # print("get employyeess of",pk,"company")
        try:
            company=Company.objects.get(pk=pk)
            emps=Employee.objects.filter(company=company)
            emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Company doesnot exist !!! Error  '
            }
                
            )
        
     
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    
