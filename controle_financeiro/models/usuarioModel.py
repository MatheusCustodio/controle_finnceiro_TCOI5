from django.db import models

class UsuarioModel(models.Model):
    usuario_id  = models.AutoField(primary_key=True)
    usuario_nome = models.CharField(max_length=45,null=False,blank=False,verbose_name="Nome")
    usuario_email = models.CharField(max_length=45,null=False,blank=False,verbose_name="Email")
    usuario_senha = models.CharField(max_length=45,null=False,blank=False,verbose_name="Senha")

    class Meta:
        ordering = ['usuario_nome']
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.usuario_nome
