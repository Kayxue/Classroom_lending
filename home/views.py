from django.shortcuts import render
from django.views.generic.base import *

# Create your views here.


class Home(TemplateView):
    template_name = "Home/home.html"
