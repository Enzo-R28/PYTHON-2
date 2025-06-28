from django.db import models
from datetime import datetime

# Create your models here.

class Prato(models.Model):
    nome_prato = models.CharField(max_length=100)
    ingredientes = models.TextField()
    modo_preparo = models.CharField(max_length=100)
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=10)
    categoria = models.CharField(max_length=100)
    data_prato = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nome_prato
    