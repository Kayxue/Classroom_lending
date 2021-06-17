from urllib import request

from django.contrib.auth.mixins import *
from django.shortcuts import render
from django.views.generic import *
from django.urls import *
from .models import *
from django.contrib.sites.shortcuts import get_current_site


class SuperuserRequiredMixin(AccessMixin):
    def dispatch(self, req, *args, **kwargs):
        if not req.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(req, *args, **kwargs)


# Create your views here.

class AddClassroom(SuperuserRequiredMixin, CreateView):
    model = Classroom
    template_name = "ClassroomForm.html"
    fields = ["name", "place", "description"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "新增教室"
        return context

    def get_success_url(self):
        return reverse("classroomList")


class ClassroomList(ListView):
    model = Classroom
    template_name = "classroomList.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["domain"] = self.request.build_absolute_uri()
        return context


class ClassroomDetail(DetailView):
    model = Classroom
    template_name = "classroomDetail.html"


class EditClassroom(SuperuserRequiredMixin, UpdateView):
    model = Classroom
    template_name = "ClassroomForm.html"
    fields = ["name", "place", "description"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "修改教室"
        return context

    def get_success_url(self):
        return reverse("classroomList")


class DeleteClassroom(SuperuserRequiredMixin, DeleteView):
    model = Classroom
    template_name = "deleteClassroom.html"

    def get_success_url(self):
        return reverse("classroomList")
