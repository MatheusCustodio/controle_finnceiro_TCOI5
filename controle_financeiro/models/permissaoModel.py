from django.db import models

class PermissaoModel(models.Model):
    permissao_id = models.AutoField(primary_key=True)
    permissao_nome = models.CharField(max_length=45, null=False, verbose_name="Nome")
    permissao_read = models.BooleanField(verbose_name="Permissao de leitura")
    permissao_write = models.BooleanField(verbose_name="Permissao de escrita")
    permissao_delete = models.BooleanField(verbose_name="Permissao de exclusão")

    class Meta:
        ordering = ['permissao_nome']
        verbose_name = 'Permissão'
        verbose_name_plural = 'Permissões'

    def __str__(self):
        return self.permissao_nome

