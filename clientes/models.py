from django.db import models

class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=250)
    class Meta:
        db_table = 'cliente'


class Veiculo(models.Model):
    idveiculo = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=7)
    ano = models.IntegerField()
    problema = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='cliente_idcliente')
    class Meta:
        db_table = 'veiculo'