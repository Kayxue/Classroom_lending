from django.contrib.auth.mixins import *
from django.urls import *
from django.views.generic import *
from lendingSystem.models import *
from django.utils import timezone

from .models import *


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
    template_name = "ClassroomList.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # timezone.localdate()==today or (everyWeek=True and borrowDate.weekDay()==timezone.localdate().weekday())
        weekday = timezone.localdate().weekday()
        if weekday == 6:
            weekday = 1
        else:
            weekday += 2

        results = Log.objects.filter(
            Q(borrowDate=timezone.localdate()) | Q(borrowDate__week_day=weekday, everyWeek=True,
                                                   endDate__gte=timezone.localdate(),
                                                   borrowDate__lte=timezone.localdate()))
        classrooms = []
        for classroom in context["classroom_list"]:
            reservations = []
            statuses = []
            for reservation in results:
                if reservation.classroom_id == classroom.id:
                    reservations.append(reservation)
                    for i in range(0, 8):
                        if reservation.startTime <= i <= reservation.end:
                            try:
                                if statuses[i] == 0:
                                    statuses[i] = 1
                            except:
                                statuses.append(1)
                        else:
                            try:
                                if statuses[i] != 1:
                                    statuses[i] = 0
                            except:
                                statuses.append(0)
            if len(statuses) == 0:
                statuses = [0, 0, 0, 0, 0, 0, 0, 0]

            nowHour = timezone.localtime().hour
            nowMinute = timezone.localtime().minute
            if nowHour == 12 or nowHour < 8 or nowHour >= 17:
                classroom.using = False
            elif 12 < nowHour < 17:
                nowHour -= 9
                if statuses[nowHour] == 1 and nowMinute > 10:
                    classroom.using = True
                else:
                    classroom.using = False
            elif 8 <= nowHour < 12:
                nowHour -= 8
                if statuses[nowHour] == 1 and nowMinute > 10:
                    classroom.using = True
                else:
                    classroom.using = False

            classroom.statuses = statuses
            classroom.reservation = reservations
            classrooms.append(classroom)

        context["classroom_list"] = classrooms
        return context


class ClassroomDetail(DetailView):
    model = Classroom
    template_name = "ClassroomDetail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = Log.objects.filter(classroom_id=self.kwargs["pk"])
        reservations = []
        for result in results:
            if result.borrowDate == timezone.localdate() or (result.borrowDate <= timezone.localdate() <= result.endDate and result.borrowDate.weekday() == timezone.localdate().weekday() and result.everyWeek == True):
                result.today = True
            else:
                result.today = False
            reservations.append(result)

        context["reservations"] = reservations
        return context


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
    template_name = "DeleteClassroom.html"

    def get_success_url(self):
        return reverse("classroomList")
