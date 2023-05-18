from django.urls import path
from .views import LoginView

from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', views.UserAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserAPIViewSingle.as_view(), name='user-detail'),

]