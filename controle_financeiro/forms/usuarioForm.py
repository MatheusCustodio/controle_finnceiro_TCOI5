from django import forms
from ..models import UsuarioModel

class UsuarioForm(forms.ModelForm):
    usuario_nome = forms.CharField(required=True, label="Nome")
    usuario_email = forms.EmailField(required=True, label="Email", widget=forms.EmailInput())
    usuario_senha = forms.CharField(required=True, label="Senha",widget=forms.PasswordInput())

    class Meta:
        model = UsuarioModel
        fields = [
            'usuario_nome',
            'usuario_email'
        ]
