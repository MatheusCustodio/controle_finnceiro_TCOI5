from django.db import models

class GrupoModel(models.Model):
    grupo_id = models.AutoField(primary_key=True)
    grupo_nome = models.CharField(max_length=45, null=False, verbose_name="Nome")

    class Meta:
        ordering = ['grupo_nome']
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'

    def __str__(self):
        return self.grupo_nome

