# coding: utf-8
from django.urls import include, path,re_path
from django.contrib import admin
from app.views import DoctorList, ReceptionView
import app.views


urlpatterns = [
    path('', DoctorList.as_view(), name='start'),
    re_path('doctor/(?P<doctor_id>\d+)/',ReceptionView.as_view(), name='reception'),
    path('date_from_ajax/', app.views.date_from_ajax, name='date_from_ajax'),

    path('admin/', admin.site.urls),
]
