from django.urls import path
from .views import LoginView

from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('login/', LoginView.as_view(), name='login'),
]