from django.db import models

# Create your models here.

class Gato(models.Model):
    nome =  models.CharField(max_length=20)
    raca = models.CharField(max_length=20)
    cores = (
      ( 'PRETO', 'Preto' ),
      ( 'AZUL', 'Azul' ),
      ( 'BRANCO', 'Branco' ),
      ( 'PARDO', 'Pardo' )
    ) 
    cor = models.CharField(choices=cores, max_length=20)
    idade = models.IntegerField()
