from django.db.models import *
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    department = CharField("單位", max_length=10)

    extension = CharField("分機", max_length=3)
