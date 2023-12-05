from django.db import models


class Mecanico(models.Model):
    idmecanico = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    especialidade = models.CharField(max_length=100)
    class Meta:
        db_table = 'mecanico'


class Equipe(models.Model):
    idequipe = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE, db_column='mecanico_idmecanico')

    class Meta:
        db_table = 'equipe'
