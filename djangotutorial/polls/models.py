import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Data da publicação")

    # @admin.display(
    #         boolean = True,
    #         ordering = "pub_date",
    #         description = "publicado_recentemente?",
    # )
    def publicado_recentemente(self):
        now = timezone.now()
        #return self.pub_date >= timezone.now()-datetime.timedelta(days=1)
        return "Sim" if now -datetime.timedelta(days=1) <= self.pub_date <= now else "Não"
    
    def inserido_por(self):
        return 'NATAN'

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) :
        return self.choice_text
    

class AuthorAdmin(admin.ModelAdmin):
    empty_value_diplay = "-empty-"