from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),        
   #path("",include('libraryapp.urls')),
    path("api/",include('rest.urls')), 
    path("login/",include('loginapp.urls')),
    path("test/",include("snippet.urls"))
]
