from django.db import models
from empresa.models import Empresa


class Ferias(models.Model):
    id_empresa = models.ForeignKey(Empresa, blank=True, on_delete=None)
    id_funcionario = models.IntegerField(blank=True)
    id_vinculo = models.IntegerField(blank=True)
    id_per_aquisitivo = models.IntegerField(blank=True)
    nome = models.CharField(max_length=80, null=True)
    inicio_per_aquisitivo = models.DateField(null=True)
    fim_per_aquisitivo = models.DateField(null=True)
    faltas_nao_justificadas = models.DecimalField(max_digits=15, decimal_places=2,null=True)
    dias_gozados = models.IntegerField(blank=True, null=True)
    inicio_per_concessivo = models.DateField(null=True)
    fim_per_concessivo = models.DateField(null=True)
    datalimite = models.DateField(null=True)
    avisoprazo = models.DateField(null=True)
    dias_direito = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    dias_abono = models.IntegerField(blank=True, null=True)
    dias_saldo = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    status = models.CharField(max_length=30, null=True)
    dias_com_deducao_faltas = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    dias_saldo_v2 = models.DecimalField(max_digits=15, decimal_places=2, null=True)

    class Meta:
        unique_together = (('id_empresa', 'id_funcionario', 'id_vinculo', 'id_per_aquisitivo'),)


