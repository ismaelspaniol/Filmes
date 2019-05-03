from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Filme(models.Model):
    titulo = models.CharField(max_length=80, null=True)
    categoria = models.CharField(max_length=80, null=True)
    sinopse = models.CharField(max_length=80000, null=True)
    ano = models.IntegerField(blank=True, null=True)
    videofile = models.FileField(upload_to='filmes/', null=True, verbose_name="", blank=True)

    def __str__(self):
        return self.titulo

@receiver(post_delete, sender=Filme)
def submission_delete(sender, instance, **kwargs):
    instance.videofile.delete(False)

