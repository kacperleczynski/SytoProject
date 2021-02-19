from django.contrib import admin
from sytoapp.models import NewWorker, CurrentWorker, Event, NewHomeWorker, CurrentHomeWorker, HomeworkersEvent

# Register your models here.

admin.site.register(NewWorker)
admin.site.register(CurrentWorker)
admin.site.register(Event)
admin.site.register(NewHomeWorker)
admin.site.register(CurrentHomeWorker)
admin.site.register(HomeworkersEvent)