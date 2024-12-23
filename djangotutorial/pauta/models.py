from django.db import models

# Create your models here.
class Pauta(models.Model):
    data = models.DateField('Data')
    hora = models.TimeField('Hora')
    nome = models.CharField('Nome', max_length=50)
    situacao = models.CharField('Sitauação', max_length=200)

    def __str__(self):
        return self.nome