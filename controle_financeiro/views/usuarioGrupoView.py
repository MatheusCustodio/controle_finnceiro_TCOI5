from django.shortcuts import render, redirect, get_object_or_404
from ..forms import UsuarioGrupoForm
from ..models import UsuarioGrupoModel, UsuarioModel, GrupoModel

def listar(request):
    form = UsuarioGrupoModel.objects.all()
    context = {
        'form':form
    }
    return render(request, 'usuarioGrupo/listar.html', context)

def inserir(request):
    form = UsuarioGrupoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_usuario_grupo')
    context = {
        'form':form
    }
    return render(request, 'usuarioGrupo/novo.html', context)


def remover(request, idUsuario, idGrupo):
    usuario = get_object_or_404(UsuarioModel, usuario_id=idUsuario)
    grupo = get_object_or_404(GrupoModel, grupo_id=idGrupo)
    usuarioGrupo = get_object_or_404(UsuarioGrupoModel, usuario=usuario, grupo=grupo)
    form = UsuarioGrupoForm(request.POST or None, instance=usuarioGrupo)
    if request.method == 'POST':
        grupo.delete()
        return redirect('listar_usuario_grupo')
    context={
        'form':form
    }
    return render(request, 'usuarioGrupo/novo.html', context)



