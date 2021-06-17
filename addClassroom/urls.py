from django.urls import *
from .views import *
from django.views.generic import *

urlpatterns = [
    path("", ClassroomList.as_view(), name="classroomList"),
    path("addclassroom/", AddClassroom.as_view(), name="addClassroom"),
    path("<int:pk>/detail/", ClassroomDetail.as_view(), name="classroomDetail"),
    path("<int:pk>/edit/", EditClassroom.as_view(), name="editClassroom"),
    path("<int:pk>/delete/", DeleteClassroom.as_view(), name="deleteClassroom")
]
