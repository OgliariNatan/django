# filepath: /c:/Users/AULA-1/Documents/GitHub/django/djangotutorial/pauta/urls.py
from django.urls import path
from . import views

app_name = 'pauta'

urlpatterns = [
    path('', views.index, name='index'),
]