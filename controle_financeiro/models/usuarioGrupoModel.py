from django.db import models
from .grupoModel import GrupoModel
from .usuarioModel import UsuarioModel
from datetime import datetime

class UsuarioGrupoModel(models.Model):
    usuario = models.ForeignKey(UsuarioModel, on_delete=models.CASCADE)
    grupo = models.ForeignKey(GrupoModel, on_delete=models.CASCADE)
    data_cadastro = models.DateField(null=False, verbose_name='Data de Cadastro', default=datetime.now)
    data_entrada = models.DateField(verbose_name='Data de entrada', null=True)
    data_saida = models.DateField(verbose_name='Data de Saida', null=True)

    class Meta:
        ordering = ['data_cadastro']
        verbose_name = 'UsuarioGrupo'
        verbose_name_plural = 'UsuariosGrupos'
        unique_together = (("usuario","grupo"))

    def __str__(self):
        return self.usuario.usuario_nome + self.grupo.grupo_nome

