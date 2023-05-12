from . import views
from django.urls import path
urlpatterns = [
    path("", views.index, name='index'), path(
        "student/", views.student_list, name="list"),
    path("student/<int:pk>", views.student_details, name="student")


]
