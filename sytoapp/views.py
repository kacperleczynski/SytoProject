from django.contrib.auth import authenticate, login, logout
from sytoapp.forms import UserForm, CurrentWorkerForm, NewWorkerForm, NewHomeworkerForm, CurrentHomeworkerForm, HomeworkersEventForm
from django.contrib.auth.models import Group
from datetime import datetime, date
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta
import calendar
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .utils import Calendar, HomeworkersCalendar,AdminHomeworkersCalendar, AdminCalendar, TestCalendar
from .forms import EventForm
from django.db.models import F, ExpressionWrapper, fields, Avg
from django.utils import translation
from django.utils.translation import gettext as _
from django.db.models import F, ExpressionWrapper, fields, Sum, Count


# Create your views here.


def main(request):
    return render(request, 'sytoapp/main.html')


def index(request):
    return render(request, 'sytoapp/index.html')


def choose_register(request):
    return render(request, 'sytoapp/choose_register.html')


def homeworkers_choose_register(request):
    return render(request, 'sytoapp/homeworkers_choose_register.html')


def homeworkers_main(request):
    return render(request, 'sytoapp/homeworkers_main.html')


def new_homeworker_register(request):
    group = Group.objects.get(name='homeworkers')
    new_worker = Group.objects.get(name='new_worker')
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        new_homeworker_form = NewHomeworkerForm(request.POST, request.FILES)

        if user_form.is_valid() and new_homeworker_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            group.user_set.add(user)
            new_worker.user_set.add(user)
            new_homeworker = new_homeworker_form.save(commit=False)
            new_homeworker.user = user
            new_homeworker.save()
            registered = True
        else:
            print(user_form.errors, new_homeworker_form.errors)

    else:
        user_form = UserForm()
        new_homeworker_form = NewHomeworkerForm()

    content = {'user_form': user_form,
               'new_homeworker_form': new_homeworker_form,
               'registered': registered}
    return render(request, 'sytoapp/new_homeworkers_register.html', content)


def new_worker_register(request):
    registered = False
    group = Group.objects.get(name='stationary_workers')
    new_worker = Group.objects.get(name='new_worker')

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        new_worker_form = NewWorkerForm(request.POST, request.FILES)

        if user_form.is_valid() and new_worker_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            group.user_set.add(user)
            new_worker.user_set.add(user)
            new_worker = new_worker_form.save(commit=False)
            new_worker.user = user
            new_worker.save()
            registered = True
        else:
            print(user_form.errors, new_worker_form.errors)

    else:
        user_form = UserForm()
        new_worker_form = NewWorkerForm()

    content = {'user_form': user_form,
               'new_worker_form': new_worker_form,
               'registered': registered}
    return render(request, 'sytoapp/new_workers_register.html', content)


def current_worker_register(request):
    group = Group.objects.get(name='stationary_workers')
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        current_worker_form = CurrentWorkerForm(request.POST, request.FILES)

        if user_form.is_valid() and current_worker_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            group.user_set.add(user)
            current_worker = current_worker_form.save(commit=False)
            current_worker.user = user
            current_worker.save()
            registered = True
        else:
            print(user_form.errors, current_worker_form.errors)

    else:
        user_form = UserForm()
        current_worker_form = NewWorkerForm()

    content = {'user_form': user_form,
               'current_worker_form': current_worker_form,
               'registered': registered}
    return render(request, 'sytoapp/current_workers_register.html', content)


def current_homeworker_register(request):
    group = Group.objects.get(name='homeworkers')
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        current_homeworker_form = CurrentHomeworkerForm(request.POST, request.FILES)

        if user_form.is_valid() and current_homeworker_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            group.user_set.add(user)
            current_homeworker = current_homeworker_form.save(commit=False)
            current_homeworker.user = user
            current_homeworker.save()
            registered = True
        else:
            print(user_form.errors, current_homeworker_form.errors)

    else:
        user_form = UserForm()
        current_homeworker_form = CurrentHomeworkerForm()

    content = {'user_form': user_form,
               'current_homeworker_form': current_homeworker_form,
               'registered': registered}
    return render(request, 'sytoapp/current_homeworkers_register.html', content)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('sytoapp:index2')

        else:
            return HttpResponse("Konto nieaktywne")

    else:
        return render(request, 'sytoapp/login.html')


def homeworkers_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('sytoapp:index3')

        else:
            return HttpResponse("Konto nieaktywne")

    else:
        return render(request, 'sytoapp/homeworkers_login.html')


def logoutUser(request):
    logout(request)
    return redirect("sytoapp:main")


def logout_homeworkers(request):
    logout(request)
    return redirect("sytoapp:main")




def index2(request):
    return render(request, 'sytoapp/index2.html')


def index3(request):
    return render(request, 'sytoapp/index3.html')


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


class CalendarView(LoginRequiredMixin,generic.ListView):
    login_url = 'signup'
    model = Event
    template_name = 'sytoapp/calendar.html'

    def get_context_data(self,**kwargs,):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        # print(d.month)
        html_cal = cal.formatmonth(withyear=True, request=self.request)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


class HomeworkersCalendarView(LoginRequiredMixin, generic.ListView):
    login_url = 'signup'
    model = HomeworkersEvent
    template_name = 'sytoapp/homeworkers_calendar.html'

    def get_context_data(self,**kwargs,):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal2 = HomeworkersCalendar(d.year, d.month)
        # print(d.month)
        html_cal = cal2.formatmonth(withyear=True, request=self.request)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

# @login_required(login_url='signup')
def create_event(request):
    form = EventForm(request.POST or None)
    if request.POST and form.is_valid():
        start_time = form.cleaned_data['start_time']
        end_time = form.cleaned_data['end_time']
        Event.objects.get_or_create(
            user=request.user,
            start_time=start_time,
            end_time=end_time
        )
        return HttpResponseRedirect(reverse('sytoapp:calendar'))
    return render(request, 'sytoapp/event.html', {'form': form})


def create_homeworkers_event(request):
    form = HomeworkersEventForm(request.POST or None)
    if request.POST and form.is_valid():
        start_day = form.cleaned_data['start_day']
        end_day = form.cleaned_data['end_day']
        day_quantity=form.cleaned_data['day_quantity']
        people_quantity=form.cleaned_data['people_quantity']

        HomeworkersEvent.objects.get_or_create(
            user=request.user,
            start_day=start_day,
            end_day=end_day,
            day_quantity=day_quantity,
            people_quantity=people_quantity
        )
        return HttpResponseRedirect(reverse('sytoapp:homeworkers_calendar'))
    return render(request, 'sytoapp/homeworkers_event.html', {'form': form})


class EventEdit(generic.UpdateView):
    model = Event
    fields = ['title', 'description', 'start_time', 'end_time']
    template_name = 'sytoapp/event.html'


def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    context = {
        'event': event,
    }
    return render(request, 'sytoapp/event_details.html', context)


def homeworkers_event_details(request, event_id):
    homeworkers_event = HomeworkersEvent.objects.get(id=event_id)
    context = {
        'homeworkers_event':homeworkers_event
    }
    return render(request, 'sytoapp/homeworkers_event_details.html', context)
# @login_required(login_url='signup')
# def event_details(request, event_id):
#     event = Event.objects.get(id=event_id)
#     eventmember = EventMember.objects.filter(event=event)
#     context = {
#         'event': event,
#         'eventmember': eventmember
#     }
#     return render(request, 'event-details.html', context)


## Admin section

class AdminHomeworkersCalendarView(LoginRequiredMixin, generic.ListView):
    login_url = 'signup'
    model = HomeworkersEvent
    template_name = 'sytoapp/admin_homeworkers_calendar.html'

    def get_context_data(self,**kwargs,):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal2 = AdminHomeworkersCalendar(d.year, d.month)
        # print(d.month)
        html_cal = cal2.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context



class AdminStationarWorkersCalendarView(LoginRequiredMixin, generic.ListView):
    login_url = 'signup'
    model = Event
    template_name = 'sytoapp/admin_stationarworkers_calendar.html'

    def get_context_data(self,**kwargs,):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal2 = AdminCalendar(d.year, d.month)
        # print(d.month)
        html_cal = cal2.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


class TestCalendarView(generic.ListView, LoginRequiredMixin):
    model = Event
    template_name = 'sytoapp/testcalendar.html'

    def get_context_data(self,**kwargs,):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal2 = TestCalendar(d.year, d.month)
        # print(d.month)
        html_cal = cal2.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        duration = ExpressionWrapper(F('end_time') - F('start_time'), output_field=fields.DurationField())
        event = Event.objects.annotate(duration=duration).aggregate(Sum('duration'))
        print(event['duration__sum'].days)
        print(event['duration__sum'].seconds // 3600)
        context['event'] = (event['duration__sum'].seconds // 3600) + (event['duration__sum'].days) * 24
        return context



def count_users(request):
    user_quantity = NewWorker.objects.all().count()
    return render(request, 'sytoapp/new_workers_count.html', {'user_quantity':user_quantity})


def count_homeworkers_user(request):
    homeworker_quantity = NewHomeWorker.objects.all().count()
    return render(request, 'sytoapp/new_homeworkers_count.html', {'homeworker_quantity':homeworker_quantity})


def test_calendar(request):
    cal = calendar.HTMLCalendar(0)
    cal = cal.formatmonth(2019,6)
    return render(request, 'sytoapp/test.html', {'cal': cal})