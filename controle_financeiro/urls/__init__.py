from django.urls import path
from django.urls.conf import include
from .usuarioUrl import UsuarioUrl
from .grupoUrl import GrupoUrl
from .usuarioGrupoUrl import UsuarioGrupoUrl

urlpatterns = [
    path('usuario/', include(UsuarioUrl.urlpatterns)),
    path('grupo/', include(GrupoUrl.urlpatterns)),
    path('usuarioGrupo/', include(UsuarioGrupoUrl.urlpatterns))
]
