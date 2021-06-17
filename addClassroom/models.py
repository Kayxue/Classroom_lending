from django.db.models import *


# Create your models here.

class Classroom(Model):
    name = CharField("教室名稱", max_length=20)

    place = CharField("教室位置", max_length=40)

    description = TextField("教室描述")

    logInTime = DateTimeField("新增時間", auto_now_add=True)

    def __str__(self):
        return self.name

