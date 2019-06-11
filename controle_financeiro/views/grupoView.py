from django.shortcuts import render, redirect, get_object_or_404
from ..forms import GrupoForm
from ..models import GrupoModel

def listar(request):
    form = GrupoModel.objects.all()
    context = {
        'form':form
    }
    return render(request, 'grupo/listar.html', context)

def inserir(request):
    form = GrupoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_grupo')
    context = {
        'form':form
    }
    return render(request, 'grupo/novo.html', context)

def alterar(request,id):
    grupo = get_object_or_404(GrupoModel, grupo_id=id)
    form = GrupoForm(request.POST or None, instance=grupo)
    if form.is_valid():
        form.save()
        return redirect('listar_grupo')
    context = {
        'form':form
    }
    return render(request, 'grupo/novo.html', context)

def remover(request,id):
    grupo = get_object_or_404(GrupoModel, grupo_id = id)
    form = GrupoForm(request.POST or None, instance=grupo)
    if request.method == 'POST':
        grupo.delete()
        return redirect('listar_grupo')
    context={
        'form':form
    }
    return render(request, 'grupo/novo.html', context)

def exibir(request, id):
    grupo = get_object_or_404(GrupoModel, grupo_id=id)
    form = GrupoForm(request.POST or None, instance=grupo)
    if request.method == 'POST':
        return redirect('listar_grupo')
    context={
        'form':form
    }
    return render(request, 'grupo/novo.html', context)

