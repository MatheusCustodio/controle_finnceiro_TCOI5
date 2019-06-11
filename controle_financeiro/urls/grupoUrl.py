from django.urls import path
from ..views import grupoView


class GrupoUrl():
    urlpatterns = [
        path('incluir',grupoView.inserir,name='inserir_grupo'),
        path('alterar/<int:id>', grupoView.alterar, name='alterar_grupo'),
        path('excluir/<int:id>', grupoView.remover, name='remover_grupo'),
        path('consultar/<int:id>', grupoView.exibir, name='exibir_grupo'),
        path('listar', grupoView.listar, name='listar_grupo')
    ]

