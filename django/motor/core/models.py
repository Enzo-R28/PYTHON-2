from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('Email', max_length=100)
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em Estoque')
    def __str__(self):
        return f'Qtd:{self.estoque} - {self.nome}  R${self.preco:.2f}'
    