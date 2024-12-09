from django.contrib import admin
from .models import Question, Choice

# Register your models here.

admin.site.register(Question)

# @admin.register(Choice)
# class ChoiceAdmin(admin.ModelAdmin):
#     pass





#https://docs.djangoproject.com/pt-br/4.2/intro/tutorial04/