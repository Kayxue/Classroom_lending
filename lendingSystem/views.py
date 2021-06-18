from django.contrib.auth.mixins import *
from django.urls import reverse
from django.views.generic import *
from .models import *
from addClassroom.models import *

from django.shortcuts import render


# Create your views here.


class createLog(LoginRequiredMixin, CreateView):
    model = Log
    fields = ["user", "borrowDate", "startTime", "end", "everyWeek"]
    template_name = "LogForm.html"

    def get_form(self):
        form = super().get_form()
        if not self.request.user.is_superuser:
            form.fields["user"].initial = self.request.user
            form.fields["user"].disabled = True
        return form

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        classroomId = self.kwargs["classroomId"]
        ctx["classroom"] = Classroom.objects.get(id=classroomId)
        ctx["title"] = "預約登記"
        return ctx

    def form_valid(self, form):
        form.instance.classroom_id = self.kwargs["classroomId"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("classroomList")


class editLog(AccessMixin, UpdateView):
    model = Log
    fields = ["user", "classroom", "borrowDate", "startTime", "end", "everyWeek"]
    template_name = "LogForm.html"

    def get_form(self):
        form = super().get_form()
        if not self.request.user.is_superuser:
            form.fields["user"].initial = self.request.user
            form.fields["user"].disabled = True
        return form

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["title"] = "修改預約"
        return ctx

    def get_success_url(self):
        return reverse("classroomList")


class deleteLog(AccessMixin, DeleteView):
    model = Log
    template_name = "DeleteLog.html"

    def get_success_url(self):
        return reverse("classroomList")
