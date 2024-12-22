from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import Clube, Competicao, Jogo, FormatoCompeticao, PosicaoJogador, Jogador, Equipa, AssociacaoFutebol, Utilizador
from .forms import ClubeForm, CompeticaoForm, JogoForm, FormatoCompeticaoForm, PosicaoJogadorForm, JogadorForm, EquipaForm, AssociacaoFutebolForm

from django.contrib.auth import login, authenticate
#from django.shortcuts import render, redirect
#from django.contrib import messages
#from .models import Utilizador  # Certifique-se de importar o seu modelo
from django.contrib.auth import get_user_model

#from django.shortcuts import render
from django.http import HttpResponse
#from django.contrib.auth import logout
#from django.shortcuts import redirect

from .models import P_Posicao
from .forms import P_PosicaoForm
from bson import ObjectId

def dashboard(request):
    if request.user.is_authenticated:  # Verifica se o usuário está autenticado
        return render(request, 'dashboard.html', {'user': request.user})
    else:
        return HttpResponse("Você precisa fazer login!")

# Página inicial
def home(request):
    return render(request, 'home.html', {'user': request.user})

# View para listar todos os utilizadores
def lista_utilizadores(request):
    utilizadores = Utilizador.objects.all()  # Busca todos os utilizadores no banco de dados
    return render(request, 'teste_conetividade.html', {'utilizadores': utilizadores})

# --- LOGIN & REGISTER ---
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            print(f"Usuário {user.nome} autenticado com sucesso")
            login(request, user)
            print("Redirecionando para a home")
            return redirect('home')
        else:
            messages.error(request, 'Credenciais inválidas.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login


def register(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        ser_admin = 'ser_admin' in request.POST  # Verifica se foi selecionado
        
        # Define ativo como False se o usuário é admin
        is_active = not ser_admin

        # Cria um novo utilizador com a senha hash
        try:
            user = Utilizador.objects.create(
                nome=nome,
                email=email,
                palavra_passe=make_password(password),  # Armazena a senha de forma segura
                ser_admin=ser_admin,
                is_active=is_active
            )
            messages.success(request, 'Conta criada com sucesso! Faça login.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Erro ao criar conta: {e}')
    
    return render(request, 'register.html')


# --- MONGO DB ---
def listar_posicoes(request):
    posicoes = P_Posicao.objects.all()        
    return render(request, 'posicoes/listar_posicoes.html', {'posicoes': posicoes})

# View para adicionar um novo registro
def adicionar_posicao(request):
    if request.method == 'POST':
        form = P_PosicaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_posicoes')  # Nome da URL para listar posições
    else:
        form = P_PosicaoForm()
    return render(request, 'posicoes/adicionar_posicao.html', {'form': form})

# View para editar uma posição
def editar_posicao(request, id):
    posicao = get_object_or_404(P_Posicao, _id=ObjectId(id))  # Note the ObjectId conversion
    if request.method == 'POST':
        form = P_PosicaoForm(request.POST, instance=posicao)
        if form.is_valid():
            form.save()
            return redirect('listar_posicoes')
    else:
        form = P_PosicaoForm(instance=posicao)
    return render(request, 'posicoes/editar_posicao.html', {'form': form}) 

# View para apagar uma posição
def apagar_posicao(request, id):
    posicao = get_object_or_404(P_Posicao, _id=ObjectId(id))
    if request.method == 'POST':
        posicao.delete()
        return redirect('listar_posicoes')
    #return render(request, 'posicoes/apagar_posicao.html', {'posicao': posicao})


# --- TEMP ---

# --- ASSOCIAÇÕES DE FUTEBOL ---
def lista_associacaoFutebol(request):
    associacao = AssociacaoFutebol.objects.all()
    return render(request, 'associacaoFutebol/lista_associacaoFutebol.html', {'associacao': associacao})


def detalhes_associacaoFutebol(request, pk):
    associacao = get_object_or_404(AssociacaoFutebol, pk=pk)
    return render(request, 'associacaoFutebol/detalhes_associacaoFutebol.html', {'associacao': associacao})


def adicionar_associacaoFutebol(request):
    if request.method == 'POST':
        form = AssociacaoFutebolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_associacaoFutebol')
    else:
        form = AssociacaoFutebolForm()
    return render(request, 'associacaoFutebol/adicionar_associacaoFutebol.html', {'form': form})


def editar_associacaoFutebol(request, pk):
    associacao = get_object_or_404(AssociacaoFutebol, pk=pk)
    if request.method == 'POST':
        form = AssociacaoFutebolForm(request.POST, instance=associacao)
        if form.is_valid():
            form.save()
            return redirect('lista_associacaoFutebol')
    else:
        form = AssociacaoFutebolForm(instance=associacao)
    return render(request, 'associacaoFutebol/editar_associacaoFutebol.html', {'form': form})


def deletar_associacaoFutebol(request, pk):
    associacao = get_object_or_404(AssociacaoFutebol, pk=pk)
    if request.method == 'POST':
        associacao.delete()
        return redirect('lista_associacaoFutebol')
    #return render(request, 'associacaoFutebol/deletar_associacao.html', {'associacao': associacao})

def todos_associacaoFutebol(request):
    associacao = AssociacaoFutebol.objects.all().order_by('nome')  # Ordenar por Nome para melhor organização
    return render(request, 'associacaoFutebol/todos_associacaoFutebol.html', {'associacao': associacao})
    
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
    #return render(request, 'clubes/deletar_clube.html', {'clube': clube})

def todos_clubes(request):
    clubes = Clube.objects.all().order_by('nome')  # Ordenar por Nome para melhor organização
    return render(request, 'clubes/todos_clubes.html', {'clubes': clubes})
    

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
    #return render(request, 'competicoes/deletar_competicao.html', {'competicao': competicao})

def todos_competicoes(request):
    competicoes = Competicao.objects.all().order_by('ano', 'nome')  # Ordenar por Ano e Nome para melhor organização
    return render(request, 'competicoes/todos_competicoes.html', {'competicoes': competicoes})

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
    #return render(request, 'jogos/deletar_jogo.html', {'jogo': jogo})

def detalhes_jogo(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    return render(request, 'jogos/detalhes_jogo.html')
    
def todos_jogos(request):
    jogos = Jogo.objects.all().order_by('dia', 'hora')  # Ordenar por data e hora para melhor organização
    return render(request, 'jogos/todos_jogos.html', {'jogos': jogos})



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
    #return render(request, 'formatoCompeticao/deletar_formatoCompeticao.html', {'formato': formato})

# --- JOGADORES ---
def lista_jogadores(request):
    jogadores = Jogador.objects.all()
    return render(request, 'jogadores/lista_jogadores.html', {'jogadores': jogadores})

def detalhes_jogador(request, pk):
    jogador = get_object_or_404(Jogador, pk=pk)
    return render(request, 'jogadores/detalhes_jogador.html', {'jogador': jogador})

def adicionar_jogador(request):
    if request.method == 'POST':
        form = JogadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_jogadores')
    else:
        form = JogadorForm()
    return render(request, 'jogadores/adicionar_jogador.html', {'form': form})

def editar_jogador(request, pk):
    jogador = get_object_or_404(Jogador, pk=pk)
    if request.method == 'POST':
        form = JogadorForm(request.POST, instance=jogador)
        if form.is_valid():
            form.save()
            return redirect('lista_jogadores')
    else:
        form = JogadorForm(instance=jogador)
    return render(request, 'jogadores/editar_jogador.html', {'form': form})

def deletar_jogador(request, pk):
    jogador = get_object_or_404(Jogador, pk=pk)
    if request.method == 'POST':
        jogador.delete()
        return redirect('lista_jogadores')
    #return render(request, 'jogadores/deletar_jogador.html', {'jogador': jogador})

def todos_jogadores(request):
    jogadores = Jogador.objects.all().order_by('nome', 'num_camisola')  # Ordenar por Nome e Número Camisola para melhor organização
    return render(request, 'jogadores/todos_jogadores.html', {'jogadores': jogadores})
    
# --- EQUIPAS ---
def lista_equipas(request):
    equipas = Equipa.objects.all()
    return render(request, 'equipas/lista_equipa.html', {'equipas': equipas})

def adicionar_equipa(request):
    if request.method == 'POST':
        form = EquipaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_equipas')
    else:
        form = EquipaForm()
    return render(request, 'equipas/adicionar_equipa.html', {'form': form})

def editar_equipa(request, pk):
    equipa = get_object_or_404(Equipa, pk=pk)
    if request.method == 'POST':
        form = EquipaForm(request.POST, instance=equipa)
        if form.is_valid():
            form.save()
            return redirect('lista_equipas')
    else:
        form = EquipaForm(instance=equipa)
    return render(request, 'equipas/editar_equipa.html', {'form': form})

def deletar_equipa(request, pk):
    equipa = get_object_or_404(Equipa, pk=pk)
    if request.method == 'POST':
        equipa.delete()
        return redirect('lista_equipas')
    #return render(request, 'equipas/deletar_equipa.html', {'equipa': equipa})
   