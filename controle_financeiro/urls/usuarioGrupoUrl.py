from django.urls import path
from ..views import usuarioGrupoView


class UsuarioGrupoUrl():
    urlpatterns = [
        path('incluir',usuarioGrupoView.inserir,name='inserir_usuario_grupo'),
        path('excluir/<int:idUsuario>/<int:idGrupo>', usuarioGrupoView.remover, name='remover_usuario_grupo'),
        path('listar', usuarioGrupoView.listar, name='listar_usuario_grupo')
]