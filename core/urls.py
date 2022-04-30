from django import views
from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]
