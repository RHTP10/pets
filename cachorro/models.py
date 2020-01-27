from django.db import models

# Create your models here.
class Cachorro(models.Model):
    nome =  models.CharField(max_length=20)
    raca = models.CharField(max_length=20)
    cores = (
      ( 'PRETO', 'Preto' ),
      ( 'CARAMELO', 'Caramelo' ),
      ( 'BRANCO', 'Branco' ),
      ( 'PARDO', 'Pardo' ),
    ) 
    cor = models.CharField(choices=cores, max_length= 20)
    idade = models.IntegerField()