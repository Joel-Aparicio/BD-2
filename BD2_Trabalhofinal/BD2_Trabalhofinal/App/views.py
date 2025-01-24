from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages

from django.contrib.auth import login, authenticate
#from django.shortcuts import render, redirect
#from django.contrib import messages
#from .models import Utilizador  # Certifique-se de importar o seu modelo
from django.contrib.auth import get_user_model

#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
#from django.contrib.auth import logout
#from django.shortcuts import redirect

from .models import P_Posicao, P_Associacao, P_FormatoCompeticao, P_Estadio, P_Jogador, P_Clube, P_Equipa, P_Competicao, P_Jogo
from .models import Utilizador
from .forms import P_PosicaoForm, P_AssociacaoForm, P_FormatoCompeticaoForm, P_EstadioForm, P_JogadorForm, P_ClubeForm, P_EquipaForm, P_CompeticaoForm, P_JogoForm
from bson import ObjectId

from django.db.models import Q
from itertools import groupby
from operator import attrgetter



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

import logging

logger = logging.getLogger(__name__)

def register(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()
        ser_admin = 'ser_admin' in request.POST
        is_active = not ser_admin

        # Verificar se os campos obrigatórios estão preenchidos
        if not nome or not email or not password:
            messages.error(request, 'Por favor, preencha todos os campos obrigatórios.')
            return render(request, 'register.html')

        # Validar se as senhas coincidem
        if password != confirm_password:
            messages.error(request, 'As senhas não coincidem!')
            return render(request, 'register.html')

        logger.debug(f"Dados recebidos: nome={nome}, email={email}, ser_admin={ser_admin}")

        try:
            # Criação do utilizador na base de dados
            user = Utilizador.objects.create(
                nome=nome,
                email=email,
                palavra_passe=make_password(password),
                ser_admin=ser_admin,
                is_active=is_active
            )
            logger.debug(f"Utilizador criado: {user}")
            messages.success(request, 'Conta criada com sucesso! Faça login.')
            return redirect('login')
        except Exception as e:
            logger.error(f"Erro ao criar utilizador: {e}")
            messages.error(request, f'Erro ao criar conta: {e}')

    return render(request, 'register.html')


# --- MONGO DB ---
## --- Posições de Campo ---
def listar_posicoes(request):
    posicoes = P_Posicao.objects.all()        
    return render(request, 'posicoes/listar_posicoes.html', {'posicoes': posicoes})

def adicionar_posicao(request):
    if request.method == 'POST':
        form = P_PosicaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_posicoes')  # Nome da URL para listar posições
    else:
        form = P_PosicaoForm()
    return render(request, 'posicoes/adicionar_posicao.html', {'form': form})

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

def apagar_posicao(request, id):
    posicao = get_object_or_404(P_Posicao, _id=ObjectId(id))
    if request.method == 'POST':
        posicao.delete()
        return redirect('listar_posicoes')
    
## --- Associações de Futebol ---
def listar_associacoes(request):
    associacoes = P_Associacao.objects.all()        
    return render(request, 'associacoes/listar_associacoes.html', {'associacoes': associacoes})

def adicionar_associacao(request):
    if request.method == 'POST':
        form = P_AssociacaoForm(request.POST)
        if form.is_valid():
            associacao = form.save(commit=False)
            # Tratar de strings vazias para campos opcionais
            if not associacao.url:
                associacao.url = None
            if not associacao.imagem:
                associacao.imagem = None
            associacao.save()
            return redirect('listar_associacoes')
    else:
        form = P_AssociacaoForm()
    return render(request, 'associacoes/adicionar_associacao.html', {'form': form})

def editar_associacao(request, id):
    associacao = get_object_or_404(P_Associacao, _id=ObjectId(id))  # Note the ObjectId conversion
    if request.method == 'POST':
        form = P_AssociacaoForm(request.POST, instance=associacao)
        if form.is_valid():
            form.save()
            return redirect('listar_associacoes')
    else:
        form = P_AssociacaoForm(instance=associacao)
    return render(request, 'associacoes/editar_associacao.html', {'form': form}) 
    
def apagar_associacao(request, id):
    associacao = get_object_or_404(P_Associacao, _id=ObjectId(id))
    if request.method == 'POST':
        associacao.delete()
        return redirect('listar_associacoes')
        
def todas_associacoes(request):
    associacao = P_Associacao.objects.all().order_by('nome')  # Ordenar por Nome para melhor organização
    return render(request, 'associacoes/todas_associacoes.html', {'associacao': associacao})

def detalhes_associacao(request, id):
    associacao = get_object_or_404(P_Associacao, _id=ObjectId(id))
    return render(request, 'associacoes/detalhes_associacao.html', {'associacao': associacao})
    
## --- Formatos de Competições ---
def listar_formatos(request):
    formatos = P_FormatoCompeticao.objects.all()
    return render(request, 'formatos/listar_formatos.html', {'formatos': formatos})

def adicionar_formato(request):
    if request.method == 'POST':
        form = P_FormatoCompeticaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_formatos')
    else:
        form = P_FormatoCompeticaoForm()
    return render(request, 'formatos/adicionar_formato.html', {'form': form})

def editar_formato(request, id):
    formato = get_object_or_404(P_FormatoCompeticao, _id=ObjectId(id))
    if request.method == 'POST':
        form = P_FormatoCompeticaoForm(request.POST, instance=formato)
        if form.is_valid():
            form.save()
            return redirect('listar_formatos')
    else:
        form = P_FormatoCompeticaoForm(instance=formato)
    return render(request, 'formatos/editar_formato.html', {'form': form})

def apagar_formato(request, id):
    formato = get_object_or_404(P_FormatoCompeticao, _id=ObjectId(id))
    if request.method == 'POST':
        formato.delete()
        return redirect('listar_formatos')

## --- Estádios ---
def listar_estadios(request):
    estadios = P_Estadio.objects.all().order_by('nome')  # Ordenar por Nome para melhor organização
    return render(request, 'estadios/listar_estadios.html', {'estadios': estadios})

def adicionar_estadio(request):
    if request.method == 'POST':
        form = P_EstadioForm(request.POST)
        if form.is_valid():
            estadio = form.save(commit=False)
            # Tratar de strings vazias para campos opcionais
            if not estadio.imagem:
                estadio.imagem = None
            estadio.save()
            return redirect('listar_estadios')
    else:
        form = P_EstadiosForm()
    return render(request, 'estadios/adicionar_estadio.html', {'form': form})

def editar_estadio(request, id):
    estadio = get_object_or_404(P_Estadio, _id=ObjectId(id))
    if request.method == 'POST':
        form = P_EstadioForm(request.POST, instance=estadio)
        if form.is_valid():
            form.save()
            return redirect('listar_estadios')
    else:
        form = P_EstadioForm(instance=estadio)
    return render(request, 'estadios/editar_estadio.html', {'form': form})

def apagar_estadio(request, id):
    estadio = get_object_or_404(P_Estadio, _id=ObjectId(id))
    if request.method == 'POST':
        estadio.delete()
        return redirect('listar_estadios')

def todos_estadios(request):
    estadio = P_Estadio.objects.all().order_by('nome')  # Ordenar por Nome para melhor organização
    return render(request, 'estadios/todos_estadios.html', {'estadio': estadio})
    
def detalhes_estadio(request, id):
    estadio = get_object_or_404(P_Estadio, _id=ObjectId(id))
    return render(request, 'estadios/detalhes_estadio.html', {'estadio': estadio})
    
## --- Jogadores ---
def listar_jogadores(request):
    jogadores = P_Jogador.objects.all().order_by('nome', 'num_camisola')  # Ordenar por Nome e Número de Camisola para melhor organização
    return render(request, 'jogadores/listar_jogadores.html', {'jogadores': jogadores})

def adicionar_jogador(request):
    if request.method == 'POST':
        form = P_JogadorForm(request.POST)
        if form.is_valid():
            jogador = form.save(commit=False)
            # Tratar de strings vazias para campos opcionais
            if not jogador.imagem:
                jogador.imagem = None
            jogador.save()
            return redirect('listar_jogadores')
    else:
        form = P_JogadorForm()
    return render(request, 'jogadores/adicionar_jogador.html', {'form': form})
    
def editar_jogador(request, id):
    jogador = get_object_or_404(P_Jogador, _id=ObjectId(id))
    if request.method == 'POST':
        form = P_JogadorForm(request.POST, instance=jogador)
        if form.is_valid():
            form.save()
            return redirect('listar_jogadores')
    else:
        form = P_JogadorForm(instance=jogador)
    return render(request, 'jogadores/editar_jogador.html', {'form': form})
    
def apagar_jogador(request, id):
    jogador = get_object_or_404(P_Jogador, _id=ObjectId(id))
    if request.method == 'POST':
        jogador.delete()
        return redirect('listar_jogadores')
        
def todos_jogadores(request):
    jogador = P_Jogador.objects.all().order_by('nome', 'num_camisola')  # Ordenar por Nome e Número de Camisola para melhor organização
    return render(request, 'jogadores/todos_jogadores.html', {'jogador': jogador})
    
def detalhes_jogador(request, id):
    jogador = get_object_or_404(P_Jogador, _id=ObjectId(id))
    return render(request, 'jogadores/detalhes_jogador.html', {'jogador': jogador})

## --- Clubes ---
def listar_clubes(request):
    clubes = P_Clube.objects.all().order_by('nome') # Ordenar por Nome
    return render(request, 'clubes/listar_clubes.html', {'clubes': clubes})
    
def adicionar_clube(request):
    if request.method == 'POST':
        print("=== POST DATA ===")
        print(request.POST)
        form = P_ClubeForm(request.POST)
        if form.is_valid():
            clube = form.save(commit=False)
            if not clube.imagem:
                clube.imagem = None
            clube.save()
            return redirect('listar_clubes')
        else:
            print("=== FORM ERRORS ===")
            print(form.errors)
            print("=== FORM CLEANED DATA ===")
            print(form.cleaned_data if hasattr(form, 'cleaned_data') else "No cleaned data")
    else:
        form = P_ClubeForm()
    return render(request, 'clubes/adicionar_clube.html', {'form': form})
    
def editar_clube(request, id):
    clube = get_object_or_404(P_Clube, _id=ObjectId(id))
    if request.method == 'POST':
        form = P_ClubeForm(request.POST, instance=clube)
        if form.is_valid():
            form.save()
            return redirect('listar_clubes')
    else:
        form = P_ClubeForm(instance=clube)
    return render(request, 'clubes/editar_clube.html', {'form': form})
    
def apagar_clube(request, id):
    clube = get_object_or_404(P_Clube, _id=ObjectId(id))
    if request.method == 'POST':
        clube.delete()
        return redirect('listar_clubes')
        
def todos_clubes(request):
    clube = P_Clube.objects.all().order_by('nome')  # Ordenar por Nome para melhor organização
    return render(request, 'clubes/todos_clubes.html', {'clube': clube})
    
def detalhes_clube(request, id):
    clube = get_object_or_404(P_Clube, _id=ObjectId(id))
    equipas = P_Equipa.objects.filter(clube=clube)
    jogadores = P_Jogador.objects.filter(equipa__clube=clube).order_by('posicao__nome', 'nome')
    
    # Agrupar jogadores por posição
    jogadores_por_posicao = {}
    for jogador in jogadores:
        posicao_nome = jogador.posicao.nome if jogador.posicao else "Sem Posição"
        if posicao_nome not in jogadores_por_posicao:
            jogadores_por_posicao[posicao_nome] = []
        jogadores_por_posicao[posicao_nome].append(jogador)
    
    return render(request, 'clubes/detalhes_clube.html', {
        'clube': clube,
        'equipas': equipas,
        'jogadores_por_posicao': dict(sorted(jogadores_por_posicao.items()))
    })

def todos_clubes(request):
    clubes = P_Clube.objects.all().order_by('nome')  # Ordenar por Nome para melhor organização
    return render(request, 'clubes/todos_clubes.html', {'clubes': clubes})
    
## --- Equipas ---
def listar_equipas(request):
    equipas = P_Equipa.objects.all()
    return render(request, 'equipas/listar_equipas.html', {'equipas': equipas})

def adicionar_equipa(request):
    if request.method == 'POST':
        print("=== VIEW DEBUG ===")
        print("POST data:", request.POST)
        print("Clube value from POST:", request.POST.get('clube'))
        print("All available clubes:", list(P_Clube.objects.all()))
        form = P_EquipaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_equipas')
        else:
            print("Form errors:", form.errors)
    else:
        form = P_EquipaForm()
    return render(request, 'equipas/adicionar_equipa.html', {'form': form})

def editar_equipa(request, id):
    equipa = get_object_or_404(P_Equipa, _id=ObjectId(id))
    if request.method == 'POST':
        form = P_EquipaForm(request.POST, instance=equipa)
        if form.is_valid():
            form.save()
            return redirect('listar_equipas')
    else:
        form = P_EquipaForm(instance=equipa)
    return render(request, 'equipas/editar_equipa.html', {'form': form})
    
def apagar_equipa(request, id):
    equipa = get_object_or_404(P_Equipa, _id=ObjectId(id))
    if request.method == 'POST':
        equipa.delete()
        return redirect('listar_equipas')
        


## --- Competições ---
def listar_competicoes(request):
    competicoes = P_Competicao.objects.all()
    return render(request, 'competicoes/listar_competicoes.html', {'competicoes': competicoes})

def adicionar_competicao(request):
    if request.method == 'POST':
        form = P_CompeticaoForm(request.POST)
        if form.is_valid():
            competicao = form.save(commit=False)
            # Tratar de strings vazias para campos opcionais
            if not competicao.imagem:
                competicao.imagem = None
            competicao.save()
            return redirect('listar_competicoes')
    else:
        form = P_CompeticaoForm()
    return render(request, 'competicoes/adicionar_competicao.html', {'form': form})

def editar_competicao(request, id):
    competicao = get_object_or_404(P_Competicao, _id=ObjectId(id))
    if request.method == 'POST':
        form = P_CompeticaoForm(request.POST, instance=competicao)
        if form.is_valid():
            form.save()
            return redirect('listar_competicoes')
    else:
        form = P_CompeticaoForm(instance=competicao)
    return render(request, 'competicoes/editar_competicao.html', {'form': form})

def apagar_competicao(request, id):
    competicao = get_object_or_404(P_Competicao, _id=ObjectId(id))
    if request.method == 'POST':
        competicao.delete()
        return redirect('listar_competicoes')
        
def todas_competicoes(request):
    competicoes = P_Competicao.objects.all().order_by('nome')  # Ordenar por Nome para melhor organização
    return render(request, 'competicoes/todas_competicoes.html', {'competicoes': competicoes})
    
def detalhes_competicao(request, id):
    competicao = get_object_or_404(P_Competicao, _id=ObjectId(id))
    return render(request, 'competicoes/detalhes_competicao.html', {'competicao': competicao})
    
    
 # --- JOGOS ---
def listar_jogos(request):
    jogos = P_Jogo.objects.all()
    return render(request, 'jogos/listar_jogos.html', {'jogos': jogos})

def adicionar_jogo(request):
    if request.method == 'POST':
        print("=== DEBUG VIEW ===")
        print("POST data:", request.POST)
        form = P_JogoForm(request.POST)
        
        if form.is_valid():
            print("Form is valid")
            print("Cleaned data:", form.cleaned_data)
            try:
                # Tentar criar o documento diretamente no MongoDB para debug
                from django.db import connections
                from bson import ObjectId
                
                jogo = form.save(commit=False)
                print("Jogo object before save:", jogo.__dict__)
                
                # Preparar o documento para o MongoDB
                doc = {
                    '_id': ObjectId(),
                    'estado': form.cleaned_data['estado'],
                    'duracao': form.cleaned_data['duracao'],
                    'prolongamento': form.cleaned_data['prolongamento'],
                    'penaltis': form.cleaned_data['penaltis']
                }
                print("MongoDB document to be inserted:", doc)
                
                # Tentar salvar
                jogo.save()
                print("Jogo saved successfully")
                return redirect('listar_jogos')
                
            except Exception as e:
                print("Save error:", str(e))
                print("Error type:", type(e))
                print("Error details:", e.__dict__ if hasattr(e, '__dict__') else "No additional details")
                form.add_error(None, f"Erro ao salvar: {str(e)}")
        else:
            print("Form errors:", form.errors)
    else:
        form = P_JogoForm()
    
    return render(request, 'jogos/adicionar_jogo.html', {'form': form})

def editar_jogo(request, id):
    competicao = get_object_or_404(P_Competicao, _id=ObjectId(id))
    if request.method == 'POST':
        form = P_CompeticaoForm(request.POST, instance=competicao)
        if form.is_valid():
            form.save()
            return redirect('listar_competicoes')
    else:
        form = P_CompeticaoForm(instance=competicao)
    return render(request, 'competicoes/editar_competicao.html', {'form': form})

def apagar_jogo(request, id):
    competicao = get_object_or_404(P_Competicao, _id=ObjectId(id))
    if request.method == 'POST':
        competicao.delete()
        return redirect('listar_competicoes')
        
def todos_jogos(request):
    competicoes = P_Competicao.objects.all().order_by('nome')  # Ordenar por Nome para melhor organização
    return render(request, 'competicoes/todas_competicoes.html', {'competicoes': competicoes})
    
def detalhes_jogo(request, id):
    competicao = get_object_or_404(P_Competicao, _id=ObjectId(id))
    return render(request, 'competicoes/detalhes_competicao.html', {'competicao': competicao})

 # --- OUTROS ---
def get_equipas_por_clube(request, clube_id):
    try:
        print(f"Buscando equipas para o clube ID: {clube_id}")  # Debug
        clube = P_Clube.objects.get(_id=ObjectId(clube_id))
        print(f"Clube encontrado: {clube.nome}")  # Debug
        
        equipas = P_Equipa.objects.filter(clube=clube)
        print(f"Equipas encontradas: {list(equipas)}")  # Debug
        
        data = [{
            'id': str(equipa._id),
            'nome': equipa.nome
        } for equipa in equipas]
        
        print(f"Dados retornados: {data}")  # Debug
        return JsonResponse(data, safe=False)
    except Exception as e:
        print(f"Erro: {str(e)}")  # Debug
        return JsonResponse({'error': str(e)}, status=400)
        
   