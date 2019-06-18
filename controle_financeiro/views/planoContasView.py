from django.shortcuts import render, redirect, get_object_or_404
from ..forms import PlanoContasForm
from ..models import PlanoContasModel

def listar(request):
    form = PlanoContasModel.objects.all()
    context = {
        'form':form
    }
    return render(request, 'planoContas/listar.html', context)

def inserir(request):
    form = PlanoContasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_plano_conta')
    context = {
        'form':form
    }
    return render(request, 'planoContas/novo.html', context)

def alterar(request,id):
    grupo = get_object_or_404(PlanoContasModel, grupo_id=id)
    form = PlanoContasForm(request.POST or None, instance=grupo)
    if form.is_valid():
        form.save()
        return redirect('listar_plano_conta')
    context = {
        'form':form
    }
    return render(request, 'planoContas/novo.html', context)

def remover(request,id):
    grupo = get_object_or_404(PlanoContasModel, grupo_id = id)
    form = PlanoContasForm(request.POST or None, instance=grupo)
    if request.method == 'POST':
        grupo.delete()
        return redirect('listar_plano_conta')
    context={
        'form':form
    }
    return render(request, 'planoContas/novo.html', context)

def exibir(request, id):
    grupo = get_object_or_404(PlanoContasModel, grupo_id=id)
    form = PlanoContasForm(request.POST or None, instance=grupo)
    if request.method == 'POST':
        return redirect('listar_plano_conta')
    context={
        'form':form
    }
    return render(request, 'planoContas/novo.html', context)

