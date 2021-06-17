from django.contrib.auth.mixins import *
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import *
from .models import *


class SuperuserRequiredMixin(AccessMixin):
    def dispatch(self, req, *args, **kwargs):
        if not req.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(req, *args, **kwargs)


class UserList(LoginRequiredMixin, ListView):
    model = User
    ordering = ["username"]
    template_name = "UserList.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["domain"] = self.request.build_absolute_uri()
        return context


class AddUser(SuperuserRequiredMixin, CreateView):
    model = User
    fields = ["first_name", "last_name", "department", "extension", "username", "password"]
    template_name = "UserForm.html"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "新增使用者"
        return context

    def get_success_url(self):
        return reverse("userList")


class EditUser(SuperuserRequiredMixin, UpdateView):
    model = User
    fields = ["firstname", "lastname", "department", "extension", "username", "password"]
    template_name = "UserForm.html"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "修改使用者"
        return context

    def get_success_url(self):
        return reverse("userList")
