from django.urls import path
from ..views import permissaoView


class PermissaoUrl():
    urlpatterns = [
        path('incluir',permissaoView.inserir,name='inserir_permissao'),
        path('alterar/<int:id>', permissaoView.alterar, name='alterar_permissao'),
        path('excluir/<int:id>', permissaoView.remover, name='remover_permissao'),
        path('consultar/<int:id>', permissaoView.exibir, name='exibir_permissao'),
        path('listar', permissaoView.listar, name='listar_permissao')
    ]

