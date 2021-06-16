from urllib import request

from django.shortcuts import render
from django.views.generic import *
from django.urls import *
from .models import *
from django.contrib.sites.shortcuts import get_current_site


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["domain"] = self.request.build_absolute_uri()
        return context
