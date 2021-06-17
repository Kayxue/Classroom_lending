from django.urls import *
from django.views.generic import *
from .views import *

urlpatterns = [
    path("", UserList.as_view(), name="userList"),
    path("adduser/", AddUser.as_view(), name="addUser"),
    path("<int:pk>/edit/", EditUser.as_view(), name="editUser"),
    path("<int:pk>/detail/", UserDetail.as_view(), name="userDetail"),
    path("<int:pk>/delete/",DeleteUser.as_view(), name="deleteUser"),
]
