import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Data da publicação")

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
    Choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) :
        return self.Choice_text
    