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
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    search_fields = ['question_text']



admin.site.register(Question, QuestionAdmin)

# @admin.register(Choice)
# class ChoiceAdmin(admin.ModelAdmin):
#     pass





#https://docs.djangoproject.com/pt-br/4.2/intro/tutorial07/