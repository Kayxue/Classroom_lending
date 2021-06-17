from django.urls import *
from django.views.generic import *
from .views import *

urlpatterns = [
    path("", UserList.as_view(), name="userList"),
    path("adduser/", AddUser.as_view(), name="addUser"),
    path("edituser/", EditUser.as_view(), name="editUser")
]
