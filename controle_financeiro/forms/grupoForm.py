from django import forms
from ..models import GrupoModel, PermissaoModel

class GrupoForm(forms.ModelForm):
    grupo_nome = forms.CharField(required=True, label="Nome")
    grupo_permissao = forms.ModelChoiceField(queryset=PermissaoModel.objects.all(), label='permissão')

    class Meta:
        model = GrupoModel
        fields = [
            'grupo_nome'
        ]