from django.contrib import admin
from .models import  Pauta
# Register your models here.

class PautaAdmin(admin.ModelAdmin):
    list_display = ('data', 'hora', 'nome', 'situacao')
    search_fields = ('nome', 'data')
    list_filter = ('data', 'nome')

admin.site.register(Pauta, PautaAdmin)