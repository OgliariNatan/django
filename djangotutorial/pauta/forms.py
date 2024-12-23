# filepath: /c:/Users/AULA-1/Documents/GitHub/django/djangotutorial/pauta/forms.py
from django import forms
from .models import Pauta

class PautaForm(forms.ModelForm):
    class Meta:
        model = Pauta
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time','class' : 'time-input'})  # Alterar para o widget padrão de hora
        }