from django.contrib import admin
from django.urls import *
from django.views.generic import *
from .views import *

urlpatterns = [
    path("create/<int:classroomId>/", createLog.as_view(), name="createLog"),
    path("edit/<int:pk>", editLog.as_view(), name="editLog"),
    path("delete/<int:pk>", deleteLog.as_view(), name="deleteLog")
]
