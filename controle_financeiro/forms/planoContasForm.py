from django import forms
from ..models import PlanoContasModel

class PlanoContasForm(forms.ModelForm):
    plano_contas_referencial = forms.CharField(max_length=45, label="Referencial")
    plano_contas_descricao = forms.CharField(max_length=45, label="Descricao")
    plano_contas_inicio_validade = forms.DateField( label="Inicio Validade", input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'id' : 'datetimepickerInicioValidade',
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepickerInicioValidade'
        }))
    plano_contas_fim_validade = forms.DateField(label="Fim Validade", input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'id':'datetimepickerFimValidade',
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepickerFimValidade'
        }))
    plano_contas_tipo = forms.CharField(max_length=1, label="Tipo")

    class Meta:
        model = PlanoContasModel
        fields = [
            'plano_contas_referencial',
            'plano_contas_descricao',
            'plano_contas_inicio_validade',
            'plano_contas_fim_validade',
            'plano_contas_tipo'
        ]

