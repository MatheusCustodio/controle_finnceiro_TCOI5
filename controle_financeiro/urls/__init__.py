from django.urls import path
from django.urls.conf import include
from .usuarioUrl import UsuarioUrl
from .grupoUrl import GrupoUrl
from .usuarioGrupoUrl import UsuarioGrupoUrl
from .permissaoUrl import PermissaoUrl
from .planoContasUrl import PlanoContasUrl

urlpatterns = [
    path('usuario/', include(UsuarioUrl.urlpatterns)),
    path('grupo/', include(GrupoUrl.urlpatterns)),
    path('usuarioGrupo/', include(UsuarioGrupoUrl.urlpatterns)),
    path('permissao/', include(PermissaoUrl.urlpatterns)),
    path('planoContas/', include(PlanoContasUrl.urlpatterns))
]
