from django.db import models
from clientes.models import Veiculo
from mecanicos.models import Equipe

class OrdemDeServico(models.Model):
    idordem_de_servico = models.AutoField(primary_key=True)
    data_recebida = models.DateField()
    data_entrega = models.DateField()
    titulo = models.CharField(max_length=150)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, db_column='idveiculo')
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, db_column='idequipe')
    class Meta:
        db_table = 'ordem_de_servico'


