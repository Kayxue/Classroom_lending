from django.urls import *
from .views import *
from django.views.generic import *

urlpatterns = [
    path("", ClassroomList.as_view(), name="classroomList"),
    path("addclassroom/", AddClassroom.as_view(), name="addClassroom")
]
