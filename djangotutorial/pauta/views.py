from django.shortcuts import render
from .models import Pauta
# Create your views here.
def index(request):
    pautas = Pauta.objects.all().order_by('data', 'hora')
    return render(request, 'pauta/index.html',{'pautas' : pautas})