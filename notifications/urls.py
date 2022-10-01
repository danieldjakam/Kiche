from django.urls import path
from . import views

app_name = 'notifs'

urlpatterns = [
    path('', views.all_notifications, name='all'),
]