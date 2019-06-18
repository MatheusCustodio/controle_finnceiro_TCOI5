from django.urls import path
from ..views import planoContasView


class PlanoContasUrl():
    urlpatterns = [
        path('incluir',planoContasView.inserir,name='inserir_plano_conta'),
        path('alterar/<int:id>', planoContasView.alterar, name='alterar_plano_conta'),
        path('excluir/<int:id>', planoContasView.remover, name='remover_plano_conta'),
        path('consultar/<int:id>', planoContasView.exibir, name='exibir_plano_conta'),
        path('listar', planoContasView.listar, name='listar_plano_conta')
    ]

