from django.db import models


class Empresa(models.Model):
    nro_inscricao = models.CharField(max_length=14)
    razao_social = models.CharField(max_length=80)
    cod_empresa = models.IntegerField(blank=True)

    def __str__(self):
        return self.razao_social + ' ' + self.nro_inscricao
