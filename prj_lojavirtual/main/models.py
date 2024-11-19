# -*- coding: utf-8 -*-
from django.db import models
import datetime
import math
# Create your models here.

class Categoria(models.Model):
    """
    define a tabela Categoria do banco de dados
    """
    nome = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    data_criacao = models.DateTimeField(max_length=150, unique=True,db_index=True, default=datetime.datetime.now)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)

    #retorna o nome
    def __str__(self) -> str:
        return self.nome

class Produto(models.Model):
    """
    Define a tabela Produtos do banco de dados
    """
    categoria = models.ForeignKey(
        Categoria, 
        related_name="produtos", 
        null=True, 
        on_delete=models.CASCADE
        )
    nome = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    estoque = models.PositiveBigIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to="imagens-produtos", blank=True)

    def __str__(self) -> str:
        return self.nome   
    
    def save(self, *args, **kwargs):
        print("O metódo save(), foi chamado\n")
        print(f"Parâmetros *args: {args},\t**kwargs:{kwargs}")
        super(Produto, self).save(*args, **kwargs)

class Vetor(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()

    def modulo(self):
        resultado = self.x ** 2 + self.y ** 2 + self.z ** 2
        resultado = math.pow(resultado, 0.5)
        return resultado