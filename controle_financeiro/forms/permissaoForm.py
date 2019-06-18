from django import forms
from ..models import PermissaoModel

class PermissaoForm(forms.ModelForm):
    permissao_nome = forms.CharField(required=True, label="Nome")
    permissao_read = forms.BooleanField(label="leitura", required=False, widget=forms.CheckboxInput())
    permissao_write = forms.BooleanField(label="escrita", required=False, widget=forms.CheckboxInput())
    permissao_delete = forms.BooleanField(label="remoção", required=False, widget=forms.CheckboxInput())

    class Meta:
        model = PermissaoModel
        fields = [
            'permissao_nome',
            'permissao_read',
            'permissao_write',
            'permissao_delete'
        ]

