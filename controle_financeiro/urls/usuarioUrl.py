from django.urls import path
from ..views import usuarioView


class UsuarioUrl():
    urlpatterns = [
        path('incluir',usuarioView.inserir,name='inserir_usuario'),
        path('alterar/<int:id>',usuarioView.alterar,name='alterar_usuario'),
        path('excluir/<int:id>',usuarioView.remover,name='remover_usuario'),
        path('consultar/<int:id>',usuarioView.exibir,name='exibir_usuario'),
        path('listar',usuarioView.listar,name='listar_usuario'),
]
