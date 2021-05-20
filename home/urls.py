from django.urls import *
from django.views.generic import *
from .views import *

urlpatterns = [
    path("", Home.as_view())
]
