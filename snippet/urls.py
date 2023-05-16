from . import views
from django.urls import path,include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

# router=routers.DefaultRouter()
# router.register(r'snippets',views.SnippetList.as_view(),basename='snippet')



urlpatterns = [
   
#    path('', include(router.urls)),
    
    
   
   path('snippets/',views.SnippetList.as_view()),
   path('snippets/<int:pk>/',views.SnippetDetail.as_view()),
  
   

]
urlpatterns = format_suffix_patterns(urlpatterns)
