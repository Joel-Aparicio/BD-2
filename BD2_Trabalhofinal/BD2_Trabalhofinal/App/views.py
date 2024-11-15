# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Clube,Competicao, Jogo
from .forms import ClubeForm,CompeticaoForm, JogoForm

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
    
    
#JOGOS
def lista_jogos(request):
    jogos = Jogo.objects.all()
    return render(request, 'jogos/lista_jogos.html', {'jogos': jogos})
    
def adicionar_jogo(request):
    if request.method == 'POST':
        form = JogoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_jogos')  # Ajuste para a página de lista de jogos
    else:
        form = JogoForm()
    return render(request, 'jogos/adicionar_jogo.html', {'form': form})
    
def editar_jogo(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    if request.method == 'POST':
        form = JogoForm(request.POST, instance=jogo)
        if form.is_valid():
            form.save()
            return redirect('lista_jogos')  # Redireciona para a lista de jogos
    else:
        form = JogoForm(instance=jogo)
    return render(request, 'jogos/editar_jogo.html', {'form': form})

# View para deletar um jogo
def deletar_jogo(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    if request.method == 'POST':
        jogo.delete()
        return redirect('lista_jogos')  # Redireciona para a lista de jogos
    return render(request, 'jogos/deletar_jogo.html', {'jogo': jogo})