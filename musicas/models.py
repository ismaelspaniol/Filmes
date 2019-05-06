from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Genero(models.Model):
    descricao = models.CharField(max_length=80)

    def __str__(self):
        return self.descricao


class Musica(models.Model):
    nome = models.CharField(max_length=80)
    genero = models.ForeignKey(Genero, on_delete=None)
    musica_file = models.FileField(upload_to='musicas/', null=True, verbose_name="", blank=True)

    def __str__(self):
        return self.nome


@receiver(post_delete, sender=Musica)
def submission_delete(sender, instance, **kwargs):
    instance.musica_file.delete(False)




