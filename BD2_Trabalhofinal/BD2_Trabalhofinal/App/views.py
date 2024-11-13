# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Clube,Competicao
from .forms import ClubeForm,CompeticaoForm

def home(request):
    return render(request, 'home.html')
    
def lista_clubes(request):
    clubes = Clube.objects.all()
    return render(request, 'clubes/lista_clubes.html', {'clubes': clubes})

def detalhes_clube(request, pk):
    clube = get_object_or_404(Clube, pk=pk)
    return render(request, 'clubes/detalhes_clube.html', {'clube': clube})

def adicionar_clube(request):
    if request.method == 'POST':
        form = ClubeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clubes')
    else:
        form = ClubeForm()
    return render(request, 'clubes/adicionar_clube.html', {'form': form})

def editar_clube(request, pk):
    clube = get_object_or_404(Clube, pk=pk)
    if request.method == 'POST':
        form = ClubeForm(request.POST, instance=clube)
        if form.is_valid():
            form.save()
            return redirect('lista_clubes')
    else:
        form = ClubeForm(instance=clube)
    return render(request, 'clubes/editar_clube.html', {'form': form})

def deletar_clube(request, pk):
    clube = get_object_or_404(Clube, pk=pk)
    if request.method == 'POST':
        clube.delete()
        return redirect('lista_clubes')
    return render(request, 'clubes/deletar_clube.html', {'clube': clube})

def lista_competicoes(request):
    competicoes = Competicao.objects.all()
    return render(request, 'competicoes/lista_competicoes.html', {'competicoes': competicoes})

def detalhes_competicao(request, pk):
    competicao = get_object_or_404(Competicao, pk=pk)
    return render(request, 'competicoes/detalhes_competicao.html', {'competicao': competicao})

def adicionar_competicao(request):
    if request.method == 'POST':
        form = CompeticaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_competicoes')
    else:
        form = CompeticaoForm()
    return render(request, 'competicoes/adicionar_competicao.html', {'form': form})

def editar_competicao(request, pk):
    competicao = get_object_or_404(Competicao, pk=pk)
    if request.method == 'POST':
        form = CompeticaoForm(request.POST, instance=competicao)
        if form.is_valid():
            form.save()
            return redirect('lista_competicoes')
    else:
        form = CompeticaoForm(instance=competicao)
    return render(request, 'competicoes/editar_competicao.html', {'form': form})

def deletar_competicao(request, pk):
    competicao = get_object_or_404(Competicao, pk=pk)
    if request.method == 'POST':
        competicao.delete()
        return redirect('lista_competicoes')
    return render(request, 'competicoes/deletar_competicao.html', {'competicao': competicao})