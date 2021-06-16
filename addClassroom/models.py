from django.db.models import *


# Create your models here.

class Classroom(Model):
    name = CharField("教室名稱", max_length=20)

    place = CharField("教室位置", max_length=40)

    description = TextField("教室描述")
