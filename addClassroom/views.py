from django.shortcuts import render
from django.views.generic import *
from django.urls import *
from .models import *


# Create your views here.

class AddClassroom(CreateView):
    model = Classroom
    template_name = "addClassroom.html"
    fields = ["name", "place", "description"]

    def get_success_url(self):
        return reverse("classroomList")


class ClassroomList(ListView):
    model = Classroom
    template_name = "classroomList.html"
