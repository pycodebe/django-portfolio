from xml.etree.ElementInclude import include
from django import views
from django.urls import path, include
from users import views

app_name = 'users'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name="register"),
]