from django import forms
from ..models import PlanoContasModel

class PlanoContasForm(forms.ModelForm):
    plano_contas_referencial = forms.CharField(max_length=45, label="Referencial")
    plano_contas_descricao = forms.CharField(max_length=45, label="Descricao")
    plano_contas_inicio_validade = forms.DateField(label="Inicio Validade", widget=forms.DateTimeInput())
    plano_contas_fim_validade = forms.DateField(label="Fim Validade", widget=forms.DateTimeInput())
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

    def __init__(self, *args, **kwargs):
        super(PlanoContasForm, self).__init__(*args, **kwargs)
        locale_date_format = '%d/%m/%Y'
        self.fields['plano_contas_inicio_validade'].input_formats = [locale_date_format, ]
        self.fields['plano_contas_inicio_validade'].widget = forms.DateInput(format=locale_date_format,
                                                                             attrs={'class': 'form-control js-date'})
        self.fields['plano_contas_fim_validade'].input_formats = [locale_date_format, ]
        self.fields['plano_contas_fim_validade'].widget = forms.DateInput(format=locale_date_format,
                                                                          attrs={'class': 'form-control js-date'})

