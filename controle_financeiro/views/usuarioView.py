from django.shortcuts import render, redirect, get_object_or_404
from ..forms import UsuarioForm
from ..models import UsuarioModel


def listar(request):
    form = UsuarioModel.objects.all()
    context = {
        'form':form
    }
    return render(request, 'usuario/listar.html', context)

def inserir(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_usuario')
    context = {
        'form': form
    }
    return render(request, 'usuario/novo.html', context)

def alterar(request, id):
    usuario = get_object_or_404(UsuarioModel, usuario_id=id)
    form = UsuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('listar_usuario')
    context = {
        'form': form,
    }
    return render(request, 'usuario/novo.html', context)

def remover(request, id):
    usuario = get_object_or_404(UsuarioModel, pessoa_id=id)
    form = UsuarioForm(request.POST or None, instance = usuario)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuario')
    context={
        'form':form,
    }
    return render(request, 'usuario/novo.html', context)


def exibir(request, id):
    pessoa = get_object_or_404(UsuarioModel, pessoa_id=id)
    form = UsuarioForm(request.POST or None, instance = pessoa)
    if request.method == 'POST':
        return redirect('listar_usuario')
    context={
        'form':form,
    }
    return render(request, 'usuario/novo.html', context)
