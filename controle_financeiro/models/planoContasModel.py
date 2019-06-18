from django.db import models

class PlanoContasModel(models.Model):
    plano_contas_id = models.AutoField(primary_key=True)
    plano_contas_referencial = models.CharField(max_length=45, null=False, verbose_name="Referencial")
    plano_contas_descricao = models.CharField(max_length=45, null=False, verbose_name="Descricao")
    plano_contas_inicio_validade = models.DateField(null=True, verbose_name="Inicio Validade")
    plano_contas_fim_validade = models.DateField(null=True, verbose_name="Fim Validade")
    plano_contas_tipo = models.CharField(max_length=1, null=False, verbose_name="Tipo")

    class Meta:
        ordering = ['plano_contas_descricao']
        verbose_name = 'PlanoConta'
        verbose_name_plural = 'PlanosContas'

    def __str__(self):
        return self.plano_contas_descricao

