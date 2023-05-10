from . import views
from django.urls import path
urlpatterns = [
     path("",views.index,name='index'),
     path('login/',views.login,name="login"),
     path('issue/',views.issue,name="issue"),
     path('register/', views.register, name='register'),
     path('profile/', views.profile, name='profile'),
     path('renew/', views.renew, name='renew'),  
     path("logout/",views.logout,name="logout"),

    ]