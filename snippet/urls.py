from . import views
from django.urls import path,include
from rest_framework import routers

# router=routers.DefaultRouter()
# router.register(r'snippet',views.StudentViewSet,basename='snippet')



urlpatterns = [
   
    # path('', include(router.urls)),
    
    path('snippet/',views.snippet_list),
    path('snippet/<int:pk>/',views.snippet_detail),
  
   

]
