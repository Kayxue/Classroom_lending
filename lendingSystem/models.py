from django.db.models import *
from userManagement.models import *
from addClassroom.models import *


# Create your models here.
class Log(Model):
    choice = [
        (0, "第一節"),
        (1, "第二節"),
        (2, "第三節"),
        (3, "第四節"),
        (4, "第五節"),
        (5, "第六節"),
        (6, "第七節"),
        (7, "第八節"),
    ]

    user = ForeignKey(User, CASCADE, verbose_name="使用者")

    classroom = ForeignKey(Classroom, CASCADE, verbose_name="教室")

    borrowDate = DateField("借出日期")

    startTime = IntegerField("開始時間", choices=choice)

    end = IntegerField("結束時間", choices=choice)

    everyWeek = BooleanField(verbose_name="固定每週借用")

    endDate = DateField("結束日期", null=True, blank=True)
