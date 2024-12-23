# filepath: /c:/Users/AULA-1/Documents/GitHub/django/djangotutorial/pauta/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]