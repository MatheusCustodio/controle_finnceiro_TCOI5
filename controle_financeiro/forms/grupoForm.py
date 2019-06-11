from django import forms
from ..models import GrupoModel

class GrupoForm(forms.ModelForm):
    grupo_nome = forms.CharField(required=True, label="Nome")

    class Meta:
        model = GrupoModel
        fields = [
            'grupo_nome'
        ]