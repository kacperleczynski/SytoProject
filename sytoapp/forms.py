from sytoapp.models import CurrentWorker, NewWorker, Event, NewHomeWorker, CurrentHomeWorker, HomeworkersEvent
from django import forms
from django.forms import ModelForm, DateInput
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class NewWorkerForm(forms.ModelForm):
    class Meta:
        model = NewWorker
        fields = ['name', 'last_name', 'email', 'dateOfBirth', 'pesel', 'signatureImage']
        widgets = {
            'pesel': forms.TextInput(attrs={'size': 11})
        }


class NewHomeworkerForm(forms.ModelForm):
    class Meta:
        model = NewHomeWorker
        fields = ['name', 'last_name', 'email', 'dateOfBirth', 'pesel', 'signatureImage']
        widgets = {
            'pesel': forms.TextInput(attrs={'size': 11})
        }


class CurrentWorkerForm(forms.ModelForm):
    class Meta:
        model = CurrentHomeWorker
        fields = ['name', 'last_name', 'email']


class CurrentHomeworkerForm(forms.ModelForm):
    class Meta:
        model = CurrentWorker
        fields = ['name', 'last_name', 'email']


class DataInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class EventForm(ModelForm):
    class Meta:
        model = Event
        # datetime-local is a HTML5 input type, format to make date time show on fields
        widgets = {
            'start_time': DataInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': DataInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M', ),
        }
        exclude = ['user']

    #
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)


class HomeworkersEventForm(ModelForm):
    class Meta:
        model = HomeworkersEvent
        day_quantity = forms.IntegerField()
        people_quantity = forms.IntegerField()
        widgets = {
            'start_day': DataInput(),
            'end_day': DataInput(),
        }
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(HomeworkersEventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime
        self.fields['start_day'].input_formats = ('%Y-%m-%d',)
        self.fields['end_day'].input_formats = ('%Y-%m-%d',)