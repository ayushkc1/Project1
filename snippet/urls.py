from . import views
from django.urls import path,include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

# router=routers.DefaultRouter()
# router.register(r'snippets',views.snippet_list,basename='snippet')



urlpatterns = [
   
   # path('', include(router.urls)),
    
    path('snippets/',views.snippet_list),
   path('snippets/<int:pk>/',views.snippet_detail),
  
   

]
urlpatterns = format_suffix_patterns(urlpatterns)
