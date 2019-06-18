from django.db import models
from .permissaoModel import PermissaoModel

class GrupoModel(models.Model):
    grupo_id = models.AutoField(primary_key=True)
    grupo_nome = models.CharField(max_length=45, null=False, verbose_name="Nome")
    grupo_permissao = models.ForeignKey(PermissaoModel, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['grupo_nome']
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'

    def __str__(self):
        return self.grupo_nome

