from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'sytoapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('production/', views.index, name='index'),
    path('choose_register', views.choose_register, name="choose_register"),
    path('login/', views.user_login, name="login"),
    path('homeworkers_login/', views.homeworkers_login, name="homeworkers_login"),
    path('new_worker_register/', views.new_worker_register, name="new_worker"),
    path('current_worker_register/', views.current_worker_register, name='current_worker'),
    path('logout', views.logoutUser, name='logout'),
    path('homeworkers_logout', views.logout_homeworkers, name='homeworkers_logout'),
    path('index/', views.index2, name='index2'),
    path('index3/', views.index3, name='index3'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.create_event, name='event_new'),
    path('event/<int:event_id>/details/', views.event_details, name='event-detail'),
    path('homeworkers_choose_register/', views.homeworkers_choose_register, name='homeworkers_choose'),
    path('homeworkers_main/', views.homeworkers_main, name='homeworkers_main'),
    path('new_homeworker_register/', views.new_homeworker_register, name='new_homeworker'),
    path('current_homeworker_register', views.current_homeworker_register, name='current_homeworker'),
    path('homeworkers_event/new/', views.create_homeworkers_event, name='homeworkers_event_new'),
    path('homerworkers_event/<int:event_id>/details/', views.homeworkers_event_details, name='homeworkers_event-detail'),
    path('homeworkers_calendar', views.HomeworkersCalendarView.as_view(), name='homeworkers_calendar'),
    path('admin_homeworkers_calendar', views.AdminHomeworkersCalendarView.as_view(), name='admin_homeworkers_calendary'),
    path('admin_stationarworkers_calendar', views.AdminStationarWorkersCalendarView.as_view(), name='admin_stationarworkers_calendar'),
    path('test_calendar', views.TestCalendarView.as_view(), name='test_calendar'),
    path('test', views.test_calendar, name='test'),
    path('new_worker_count', views.count_users, name='count'),
    path('new_homeworker_count', views.count_homeworkers_user, name='count2')

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
