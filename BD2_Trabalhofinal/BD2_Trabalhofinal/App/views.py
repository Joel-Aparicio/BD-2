from django.shortcuts import render, get_object_or_404, redirect
from .models import Clube, Competicao, Jogo, FormatoCompeticao, PosicaoJogador
from .forms import ClubeForm, CompeticaoForm, JogoForm, FormatoCompeticaoForm, PosicaoJogadorForm

# Página inicial
def home(request):
    return render(request, 'home.html')

# --- CLUBES ---
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

# --- COMPETIÇÕES ---
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

# --- JOGOS ---
def lista_jogos(request):
    jogos = Jogo.objects.all()
    return render(request, 'jogos/lista_jogos.html', {'jogos': jogos})

def adicionar_jogo(request):
    if request.method == 'POST':
        form = JogoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_jogos')
    else:
        form = JogoForm()
    return render(request, 'jogos/adicionar_jogo.html', {'form': form})

def editar_jogo(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    if request.method == 'POST':
        form = JogoForm(request.POST, instance=jogo)
        if form.is_valid():
            form.save()
            return redirect('lista_jogos')
    else:
        form = JogoForm(instance=jogo)
    return render(request, 'jogos/editar_jogo.html', {'form': form})

def deletar_jogo(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    if request.method == 'POST':
        jogo.delete()
        return redirect('lista_jogos')
    return render(request, 'jogos/deletar_jogo.html', {'jogo': jogo})

# --- FORMATOS DE COMPETIÇÃO ---
def lista_formatoCompeticao(request):
    formatos = FormatoCompeticao.objects.all()
    return render(request, 'formatoCompeticao/lista_formatoCompeticao.html', {'formatos': formatos})

def adicionar_formatoCompeticao(request):
    if request.method == 'POST':
        form = FormatoCompeticaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_formatoCompeticao')
    else:
        form = FormatoCompeticaoForm()
    return render(request, 'formatoCompeticao/adicionar_formatoCompeticao.html', {'form': form})

def editar_formatoCompeticao(request, pk):
    formato = get_object_or_404(FormatoCompeticao, pk=pk)
    if request.method == 'POST':
        form = FormatoCompeticaoForm(request.POST, instance=formato)
        if form.is_valid():
            form.save()
            return redirect('lista_formatoCompeticao')
    else:
        form = FormatoCompeticaoForm(instance=formato)
    return render(request, 'formatoCompeticao/editar_formatoCompeticao.html', {'form': form})

def deletar_formatoCompeticao(request, pk):
    formato = get_object_or_404(FormatoCompeticao, pk=pk)
    if request.method == 'POST':
        formato.delete()
        return redirect('lista_formatoCompeticao')
    return render(request, 'formatoCompeticao/deletar_formatoCompeticao.html', {'formato': formato})

# --- POSIÇÕES DE JOGADOR ---
def lista_posicaoJogador(request):
    posicoes = PosicaoJogador.objects.all()
    return render(request, 'posicoesJogador/lista_posicaoJogador.html', {'posicoes': posicoes})

def adicionar_posicaoJogador(request):
    if request.method == 'POST':
        form = PosicaoJogadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posicaoJogador')
    else:
        form = PosicaoJogadorForm()
    return render(request, 'posicoesJogador/adicionar_posicaoJogador.html', {'form': form})

def editar_posicaoJogador(request, pk):
    posicao = get_object_or_404(PosicaoJogador, pk=pk)
    if request.method == 'POST':
        form = PosicaoJogadorForm(request.POST, instance=posicao)
        if form.is_valid():
            form.save()
            return redirect('lista_posicaoJogador')
    else:
        form = PosicaoJogadorForm(instance=posicao)
    return render(request, 'posicoesJogador/editar_posicaoJogador.html', {'form': form})

def deletar_posicaoJogador(request, pk):
    posicao = get_object_or_404(PosicaoJogador, pk=pk)
    if request.method == 'POST':
        posicao.delete()
        return redirect('lista_posicaoJogador')
    return render(request, 'posicoesJogador/deletar_posicaoJogador.html', {'posicao': posicao})
