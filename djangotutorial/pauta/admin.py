from django.contrib import admin
from .models import  Pauta
from .forms import PautaForm
from django.conf.locale.pt_BR import formats as pt_BR_formats

# Register your models here.

#define formato 24H
pt_BR_formats.TIME_FORMAT = 'H:i'
pt_BR_formats.DATETIME_FORMAT = 'd/m/Y H:i'

admin.register(Pauta)
class PautaAdmin(admin.ModelAdmin):
    form = PautaForm
    list_display = ('data', 'hora_formatada', 'nome', 'situacao')
    search_fields = ('nome', 'data')
    list_filter = ('data', 'nome')
    change_form_template = 'admin/pauta/change_form.html'  # Especifica o template personalizado

    def hora_formatada(self, obj):
        return obj.hora.strftime('%H:%M')
    hora_formatada.admin_order_field = 'hora'
    hora_formatada.short_description = 'Hora'

    
admin.site.register(Pauta, PautaAdmin)