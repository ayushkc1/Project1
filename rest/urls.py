
from . import views
from django.urls import path,include
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'students',views.StudentViewSet,basename='student')



urlpatterns = [
   
    path('', include(router.urls)),
  
   

]
