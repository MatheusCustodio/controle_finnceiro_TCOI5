from  django import forms
from ..models import UsuarioGrupoModel, UsuarioModel, GrupoModel

class UsuarioGrupoForm(forms.ModelForm):
    grupo = forms.ModelChoiceField(queryset=GrupoModel.objects.all(), label='grupo')
    usuario = forms.ModelChoiceField(queryset=UsuarioModel.objects.all(), label='usuario')
    data_cadastro = forms.DateField(required=False, label="Data de cadastro", widget=forms.DateInput(), input_formats='%d-%m-%y')

    class Meta:
        model = UsuarioGrupoModel
        fields = [
            'grupo',
            'usuario',
            'data_cadastro'
        ]

