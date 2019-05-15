from django import forms
from ..models import usuarioModel

class UsuarioForm(forms.ModelForm):
    usuario_nome = forms.CharField(required=True, label="Nome")
    usuario_email = forms.EmailField(required=True, label="Email")
    usuario_senha = forms.CharField(required=True, label="Senha",widget=forms.PasswordInput())

    class Meta:
        model = usuarioModel
        fields = [
            'usuario_nome',
            'usuario_email'
        ]
