from django.shortcuts import render, redirect, get_object_or_404
from ..forms import usuarioForm
from ..models import usuarioModel


def listar(request):
    form = usuarioModel.objects.all()
    context = {
        'form':form
    }
    return render(request, 'usuario/lista.html')

def inserir(request):
    form = usuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar')
    return render(request, 'usuario/novo.html')

def alterar(request, id):
    usuario = get_object_or_404(usuarioModel, usuario_id=id)
    form = usuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('listar')
    context = {
        'form': form,
    }
    return render(request, 'usuario/novo.html', context)