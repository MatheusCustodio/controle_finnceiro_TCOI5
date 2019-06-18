from django.shortcuts import render, redirect, get_object_or_404
from ..forms import PermissaoForm
from ..models import PermissaoModel

def listar(request):
    form = PermissaoModel.objects.all()
    context = {
        'form':form
    }
    return render(request, 'permissao/listar.html', context)

def inserir(request):
    form = PermissaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_permissao')
    context = {
        'form':form
    }
    return render(request, 'permissao/novo.html', context)

def alterar(request,id):
    grupo = get_object_or_404(PermissaoModel, grupo_id=id)
    form = PermissaoForm(request.POST or None, instance=grupo)
    if form.is_valid():
        form.save()
        return redirect('listar_permissao')
    context = {
        'form':form
    }
    return render(request, 'permissao/novo.html', context)

def remover(request,id):
    grupo = get_object_or_404(PermissaoModel, grupo_id = id)
    form = PermissaoForm(request.POST or None, instance=grupo)
    if request.method == 'POST':
        grupo.delete()
        return redirect('listar_permissao')
    context={
        'form':form
    }
    return render(request, 'permissao/novo.html', context)

def exibir(request, id):
    grupo = get_object_or_404(PermissaoModel, grupo_id=id)
    form = PermissaoForm(request.POST or None, instance=grupo)
    if request.method == 'POST':
        return redirect('listar_permissao')
    context={
        'form':form
    }
    return render(request, 'permissao/novo.html', context)

