from django.contrib import admin
from .models import Question, Choice

# Register your models here.
#class ChoiceInLine(admin.StackedInline):#alinhamento em coluna
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 2 #Numero de escolhas

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'publicado_recentemente', 'inserido_por')
    search_fields = ['question_text', "pub_date"] #define o campo de pesquisa
    list_filter = ["pub_date"] #Adiciona filtro de pesquisa
    date_hierarchy = 'pub_date'



admin.site.register(Question, QuestionAdmin)

# @admin.register(Choice)
# class ChoiceAdmin(admin.ModelAdmin):
#     pass





#https://docs.djangoproject.com/pt-br/4.2/intro/tutorial07/