from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class NewWorker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=50, null=True)
    pesel = models.CharField(max_length=11, null=True)
    dateOfBirth = models.DateField(null=True)
    signatureImage = models.ImageField(null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name + ' ' + self.last_name

    @property
    def new_worker_id(self):
        return self.id


class NewHomeWorker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=50, null=True)
    pesel = models.CharField(max_length=11, null=True)
    dateOfBirth = models.DateField(null=True)
    signatureImage = models.ImageField(null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name + ' ' + self.last_name

    @property
    def new_worker_id(self):
        return self.id


class CurrentWorker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=50, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name + ' ' + self.last_name


class CurrentHomeWorker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=50, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name + ' ' + self.last_name


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=False, auto_now=False, auto_created=False)
    end_time = models.DateTimeField(auto_now_add=False, auto_now=False, auto_created=False)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('sytoapp:event-detail', args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse('sytoapp:event-detail', args=(self.id,))
        return f'<a href="{url}"> {self.user} - {self.duration_event} godzin</a>'
    #
    @property
    def duration_event(self):
        duration = int((self.end_time - self.start_time).seconds // 3600)
        return duration


class HomeworkersEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day_quantity = models.IntegerField(null=True)
    people_quantity = models.IntegerField(null=True)
    start_day = models.DateField(auto_now_add=False, auto_now=False, auto_created=False)
    end_day = models.DateField(auto_now_add=False, auto_now=False, auto_created=False)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('sytoapp:homeworkers_event-detail', args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse('sytoapp:homeworkers_event-detail', args=(self.id,))
        return f'<a href="{url}"> {self.user} - ilość dni: {self.duration_event} </a>'

    @property
    def duration_event(self):
        return (self.end_day - self.start_day).days
