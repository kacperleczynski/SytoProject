from datetime import datetime, timedelta
from calendar import HTMLCalendar, LocaleHTMLCalendar, LocaleTextCalendar
from .models import *
import calendar


class Calendar(LocaleHTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__(locale='pl_PL')

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events, ):
        events_per_day = events.filter(start_time__day=day)
        d = ''
        print(day)
        for event in events_per_day:
            d += f'<li> {event.get_html_url} </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, events, ):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events, )
            print()
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, request, withyear=True, ):
        current_user = request.user
        events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month, user=current_user)
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events, )}\n'
        return cal


class HomeworkersCalendar(LocaleHTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(HomeworkersCalendar, self).__init__(locale='pl_PL')

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events):
        homeworkers_events_per_day = events.filter(start_day__day=day)
        d = ''
        for homeworker_event in homeworkers_events_per_day:
            d += f'<li style="color:red"> {homeworker_event.get_html_url} </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, request, withyear=True, ):
        current_user = request.user
        events = HomeworkersEvent.objects.filter(start_day__year=self.year, start_day__month=self.month,
                                                 user=current_user)
        print(events)
        cal2 = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal2 += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal2 += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal2 += f'{self.formatweek(week, events)}\n'
        return cal2


class AdminHomeworkersCalendar(LocaleHTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(AdminHomeworkersCalendar, self).__init__(locale='pl_PL')

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events):
        homeworkers_events_per_day = events.filter(start_day__day=day)
        d = ''
        for homeworker_event in homeworkers_events_per_day:
            d += f'<li class="link"> {homeworker_event.get_html_url} </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True, ):
        events = HomeworkersEvent.objects.filter(start_day__year=self.year, start_day__month=self.month, )
        cal2 = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal2 += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal2 += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal2 += f'{self.formatweek(week, events)}\n'
        return cal2


class AdminCalendar(LocaleHTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(AdminCalendar, self).__init__(locale='pl_PL')

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events, ):
        events_per_day = events.filter(start_time__day=day)
        d = ''
        print(day)
        for event in events_per_day:
            d += f'<li class="link"> {event.get_html_url} </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, events, ):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events, )
            print()
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True, ):
        events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month, )
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events, )}\n'
        return cal


class TestCalendar(LocaleHTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(TestCalendar, self).__init__(locale='pl_PL')

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events, ):
        events_per_day = events.filter(start_time__day=day)
        d = ''
        print(day)
        for event in events_per_day:
            d += f'<li> {event.get_html_url} </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, events, ):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events, )
            print()
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True, ):
        events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month, )
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events, )}\n'
        return cal
