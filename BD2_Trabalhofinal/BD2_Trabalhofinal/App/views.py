from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages



from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
#from django.shortcuts import render, redirect
#from django.contrib import messages
#from .models import Utilizador  # Certifique-se de importar o seu modelo
from django.contrib.auth import get_user_model



#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
#from django.contrib.auth import logout
#from django.shortcuts import redirect



from .models import Utilizador
from .models import P_Posicao, P_Associacao, P_FormatoCompeticao, P_Estadio, P_Jogador, P_Clube, P_Equipa, P_Competicao, P_Jogo, P_Golo, P_Falta, P_Penalti, P_Substituicao, P_ClubeFavorito
from .forms import P_PosicaoForm, P_AssociacaoForm, P_FormatoCompeticaoForm, P_EstadioForm, P_JogadorForm, P_ClubeForm, P_EquipaForm, P_CompeticaoForm, P_JogoForm
from .forms import P_PerfilForm, P_SenhaForm
from .forms import P_GoloForm, P_PenaltiForm, P_SubstituicaoForm, P_FaltaForm
from bson import ObjectId


from django.db.models import Q
from itertools import groupby
from operator import attrgetter


import logging


logger = logging.getLogger(__name__)



# Dashboard com proteção de login
@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})



# Página inicial
def home(request):
    return render(request, 'home.html')




# Lista de utilizadores
@login_required
def lista_utilizadores(request):
    utilizadores = Utilizador.objects.all()
    return render(request, 'teste_conetividade.html', {'utilizadores': utilizadores})





# View de login
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user:
            if user.is_active:  # Verificar se o utilizador está ativo
                login(request, user)
                messages.success(request, f'Bem-vindo, {user.nome}!')
                return redirect('home')
            else:
                messages.error(request, 'A sua conta está desativada.')
        else:
            messages.error(request, 'Credenciais inválidas.')

    return render(request, 'login.html')




# View de logout
def logout_view(request):
    logout(request)
    messages.success(request, 'Sessão encerrada com sucesso.')
    return redirect('home')




# Registo de utilizadores
def register(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()
        ser_admin = request.POST.get('ser_admin')  # Obter o valor do checkbox

        if not nome or not email or not password:
            messages.error(request, 'Por favor, preencha todos os campos obrigatórios.')
            return render(request, 'register.html')

        if password != confirm_password:
            messages.error(request, 'As senhas não coincidem!')
            return render(request, 'register.html')

        try:
            # Converter 'ser_admin' para booleano
            is_admin = True if ser_admin == 'on' else False  # Verifica se o checkbox está marcado
            is_active = False if is_admin else True  # Definir 'is_active' conforme 'is_admin'
            
            user = Utilizador.objects.create_user(
                email=email, nome=nome, palavra_passe=password, is_active=is_active, is_staff=is_admin
            )
            messages.success(request, 'Conta criada com sucesso! Faça login.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Erro ao criar conta: {e}')

    return render(request, 'register.html')





# --- PERFIL ---
def ver_perfil(request):
    if request.user.is_authenticated:
        # Obter o utilizador logado
        utilizador = request.user

        # Buscar clubes favoritos do utilizador
        clubes_favoritos = P_ClubeFavorito.objects.filter(utilizador_id=utilizador.utilizador_id).select_related('clube')

        # Renderizar o template com os dados do utilizador
        return render(request, 'perfil/perfil.html', {
            'utilizador': utilizador,
            'clubes_favoritos': clubes_favoritos
        })
    else:
        # Redirecionar para login caso não esteja autenticado
        return redirect('login')
        
        
        
        
        
        
def editar_perfil(request):
    if not request.user.is_authenticated:
        return redirect('login')

    utilizador = request.user
    if request.method == 'POST':
        form = P_PerfilForm(request.POST, instance=utilizador)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso.")
            return redirect('perfil')  # Redirecionar para a página de perfil
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        form = P_PerfilForm(instance=utilizador)

    return render(request, 'perfil/editar_perfil.html', {'form': form})





@login_required
def editar_senha(request):
    if request.method == "POST":
        form = P_SenhaForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            # Atualiza a sessão para que o utilizador não seja desconectado após alterar a senha
            update_session_auth_hash(request, user)
            messages.success(request, "Sua senha foi alterada com sucesso!")
            return redirect("perfil")  # Redireciona para a página de perfil
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")
    else:
        form = P_SenhaForm(user=request.user)
    
    return render(request, "perfil/editar_senha.html", {"form": form})
        
        
        
        
        
        
        
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
        form = P_EstadioForm()
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

    # Contar o número de gols do jogador
    num_golos = P_Golo.objects.filter(jogador=jogador).count()

    # Contar o número de jogos do jogador (verifica se a equipa do jogador é equipa_casa ou equipa_fora)
    num_jogos = P_Jogo.objects.filter(
        equipa_casa=jogador.equipa
    ).count() + P_Jogo.objects.filter(
        equipa_fora=jogador.equipa
    ).count()

    # Buscar todos os jogos onde o jogador participou
    jogos = P_Jogo.objects.filter(
        equipa_casa=jogador.equipa
    ) | P_Jogo.objects.filter(
        equipa_fora=jogador.equipa
    )

    context = {
        'jogador': jogador,
        'num_golos': num_golos,
        'num_jogos': num_jogos,
        'jogos': jogos.filter(estado="Terminado") #Só mostra os jogos terminados
    }

    return render(request, 'jogadores/detalhes_jogador.html', context)



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
    
    # Verificar se o clube está nos favoritos do usuário
    is_favorito = False
    if request.user.is_authenticated:
        is_favorito = P_ClubeFavorito.objects.filter(utilizador_id=request.user.utilizador_id, clube=clube).exists()

    return render(request, 'clubes/detalhes_clube.html', {
        'clube': clube,
        'equipas': equipas,
        'jogadores_por_posicao': dict(sorted(jogadores_por_posicao.items())),
        'is_favorito': is_favorito
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
    jogos = P_Jogo.objects.filter(competicao=competicao).order_by('dia', 'hora'), #Obter os jogos da competição e ordenar por Dia e Hora
    
    return render(request, 'competicoes/detalhes_competicao.html', {
        'competicao': competicao,
        'jogos': jogos
    })
    
    
    
    
    
    
    
    
    
 # --- JOGOS ---
def listar_jogos(request):
    jogos = P_Jogo.objects.all()
    return render(request, 'jogos/listar_jogos.html', {'jogos': jogos})



def adicionar_jogo(request):
    if request.method == 'POST':
        form = P_JogoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_jogos')
    else:
        form = P_JogoForm()
    return render(request, 'jogos/adicionar_jogo.html', {'form': form})




def editar_jogo(request, id):
    jogo = get_object_or_404(P_Jogo, _id=ObjectId(id))
    if request.method == 'POST':
        form = P_JogoForm(request.POST, instance=jogo)
        if form.is_valid():
            form.save()
            return redirect('listar_jogos')
    else:
        form = P_JogoForm(instance=jogo)
    return render(request, 'jogos/editar_jogo.html', {'form': form})



def apagar_jogo(request, id):
    jogo = get_object_or_404(P_Jogo, _id=ObjectId(id))
    if request.method == 'POST':
        jogo.delete()
        return redirect('listar_jogos')
       

       
def todos_jogos(request):
    jogos = P_Jogo.objects.all().order_by('dia')  # Ordenar por Dia para melhor organização
    return render(request, 'jogos/todos_jogos.html', {'jogos': jogos})
    




def detalhes_jogo(request, id):
    try:
        jogo = get_object_or_404(P_Jogo, _id=ObjectId(id))
        # Buscar todas as ações do jogo
        golos = P_Golo.objects.filter(jogo=jogo).order_by('minuto', 'compensacao')
        faltas = P_Falta.objects.filter(jogo=jogo).order_by('minuto', 'compensacao')
        substituicoes = P_Substituicao.objects.filter(jogo=jogo).order_by('minuto', 'compensacao')
        penaltis = P_Penalti.objects.filter(jogo=jogo).order_by('numero')
        
        # Filtrar os dados por clube
        golos_casa = golos.filter(clube=jogo.clube_casa)
        golos_fora = golos.filter(clube=jogo.clube_fora)
        faltas_casa = faltas.filter(clube=jogo.clube_casa)
        faltas_fora = faltas.filter(clube=jogo.clube_fora)
        substituicoes_casa = substituicoes.filter(clube=jogo.clube_casa)
        substituicoes_fora = substituicoes.filter(clube=jogo.clube_fora)
        penaltis_casa = penaltis.filter(clube=jogo.clube_casa)
        penaltis_fora = penaltis.filter(clube=jogo.clube_fora)
        
        # Count successful penalties
        total_penaltis_casa = sum(1 for p in penaltis_casa if p.golo)
        total_penaltis_fora = sum(1 for p in penaltis_fora if p.golo)
        
        return render(request, 'jogos/detalhes_jogo.html', {
            'jogo': jogo,
            'golos_casa': golos_casa,
            'golos_fora': golos_fora,
            'total_golos_casa': len(golos_casa),
            'total_golos_fora': len(golos_fora),
            'faltas_casa': faltas_casa,
            'faltas_fora': faltas_fora,
            'substituicoes_casa': substituicoes_casa,
            'substituicoes_fora': substituicoes_fora,
            'penaltis_casa': penaltis_casa,
            'penaltis_fora': penaltis_fora,
            'total_penaltis_casa': total_penaltis_casa,
            'total_penaltis_fora': total_penaltis_fora,
        })
    except Exception as e:
        print(f"Error: {str(e)}")
        raise






        
# --- ESTATISTICAS ---
def listar_estatisticas(request, id):
    try:
        jogo = get_object_or_404(P_Jogo, _id=ObjectId(id))

        estatisticas = {
            'golos': P_Golo.objects.filter(jogo=jogo).order_by('minuto', 'compensacao' ), # Ordenar pelo minuto e compensacao
            'penaltis': P_Penalti.objects.filter(jogo=jogo).order_by('numero'), # Ordenar pelo numero do penálti
            'faltas': P_Falta.objects.filter(jogo=jogo).order_by('minuto', 'compensacao' ), # Ordenar pelo minuto e compensacao
            'substituicoes': P_Substituicao.objects.filter(jogo=jogo).order_by('minuto', 'compensacao' ), # Ordenar pelo minuto e compensacao
        }

        return render(request, 'estatisticas/listar_estatisticas.html', {'jogo': jogo, 'estatisticas': estatisticas})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)







#Golos
def adicionar_golo(request, id):
    try:
        jogo = get_object_or_404(P_Jogo, _id=ObjectId(id))
        if request.method == 'POST':
            form = P_GoloForm(request.POST, jogo=jogo)
            if form.is_valid():
                golo = form.save(commit=False)
                golo.jogo = jogo
                golo.save()
                return redirect('listar_estatisticas', id=str(jogo._id))
            else:
                return JsonResponse({'error': form.errors}, status=400)
        form = P_GoloForm(jogo=jogo)
        return render(request, 'estatisticas/adicionar_golo.html', {'form': form, 'jogo': jogo})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)



def editar_golo(request, id):
    try:
        golo = get_object_or_404(P_Golo, _id=ObjectId(id))
        jogo = golo.jogo
        if request.method == 'POST':
            form = P_GoloForm(request.POST, instance=golo, jogo=jogo)
            if form.is_valid():
                form.save()
                return redirect('listar_estatisticas', id=str(jogo._id))
            else:
                return JsonResponse({'error': form.errors}, status=400)
        form = P_GoloForm(instance=golo, jogo=jogo)
        return render(request, 'estatisticas/editar_golo.html', {'form': form, 'golo': golo, 'jogo': jogo})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)




def apagar_golo(request, id):
    try:
        # Verificar se o método é POST
        if request.method == 'POST':
            # Buscar o gol usando o ID
            golo = get_object_or_404(P_Golo, _id=ObjectId(id))
            # Apagar o registro do gol
            golo.delete()
            # Redirecionar para a listagem de estatísticas ou página anterior
            return redirect('listar_estatisticas', id=golo.jogo.get_id())
        else:
            return JsonResponse({'error': 'Método não permitido'}, status=405)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
     


     
#Penáltis

def adicionar_penalti(request, id):
    try:
        jogo = get_object_or_404(P_Jogo, _id=ObjectId(id))  # Converte o id para ObjectId
        if request.method == 'POST':
            form = P_PenaltiForm(request.POST, jogo=jogo)  # Pass jogo to form
            if form.is_valid():
                penalti = form.save(commit=False)
                penalti.jogo = jogo  # Associa o penalti ao jogo
                penalti.save()
                return redirect('listar_estatisticas', id=str(jogo._id))
            else:
                return JsonResponse({'error': form.errors}, status=400)
        form = P_PenaltiForm(jogo=jogo)  # Pass jogo to form
        return render(request, 'estatisticas/adicionar_penalti.html', {'form': form, 'jogo': jogo})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)




def editar_penalti(request, id):
    try:
        penalti = get_object_or_404(P_Penalti, _id=ObjectId(id))
        jogo = penalti.jogo
        if request.method == 'POST':
            form = P_PenaltiForm(request.POST, instance=penalti, jogo=jogo)  # Pass both instance and jogo
            if form.is_valid():
                form.save()
                return redirect('listar_estatisticas', id=str(jogo._id))
            else:
                return JsonResponse({'error': form.errors}, status=400)
        form = P_PenaltiForm(instance=penalti, jogo=jogo)  # Pass both instance and jogo
        return render(request, 'estatisticas/editar_penalti.html', {'form': form, 'penalti': penalti, 'jogo': jogo})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
   

   
def apagar_penalti(request, id):
    try:
        if request.method == 'POST':
            penalti = get_object_or_404(P_Penalti, _id=ObjectId(id))
            penalti.delete()
            return redirect('listar_estatisticas', id=penalti.jogo.get_id())
        else:
            return JsonResponse({'error': 'Método não permitido'}, status=405)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
        
        
        
        
        
        
#Faltas
def adicionar_falta(request, id):
    try:
        jogo = get_object_or_404(P_Jogo, _id=ObjectId(id))
        if request.method == 'POST':
            form = P_FaltaForm(request.POST, jogo=jogo)
            if form.is_valid():
                falta = form.save(commit=False)
                falta.jogo = jogo
                falta.save()
                return redirect('listar_estatisticas', id=str(jogo._id))
            else:
                return JsonResponse({'error': form.errors}, status=400)
        form = P_FaltaForm(jogo=jogo)
        return render(request, 'estatisticas/adicionar_falta.html', {'form': form, 'jogo': jogo})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)




def editar_falta(request, id):
    try:
        falta = get_object_or_404(P_Falta, _id=ObjectId(id))
        jogo = falta.jogo
        if request.method == 'POST':
            form = P_FaltaForm(request.POST, instance=falta, jogo=jogo)
            if form.is_valid():
                form.save()
                return redirect('listar_estatisticas', id=str(jogo._id))
            else:
                return JsonResponse({'error': form.errors}, status=400)
        form = P_FaltaForm(instance=falta, jogo=jogo)
        return render(request, 'estatisticas/editar_falta.html', {'form': form, 'falta': falta, 'jogo': jogo})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
        
        
        
        
def apagar_falta(request, id):
    try:
        if request.method == 'POST':
            falta = get_object_or_404(P_Falta, _id=ObjectId(id))
            falta.delete()
            return redirect('listar_estatisticas', id=falta.jogo.get_id())
        else:
            return JsonResponse({'error': 'Método não permitido'}, status=405)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
        
        
        
        
        
#Substituições
def adicionar_substituicao(request, id):
    try:
        jogo = get_object_or_404(P_Jogo, _id=ObjectId(id))
        if request.method == 'POST':
            form = P_SubstituicaoForm(request.POST, jogo=jogo)
            if form.is_valid():
                substituicao = form.save(commit=False)
                substituicao.jogo = jogo
                substituicao.save()
                return redirect('listar_estatisticas', id=str(jogo._id))
            else:
                return JsonResponse({'error': form.errors}, status=400)
        form = P_SubstituicaoForm(jogo=jogo)
        return render(request, 'estatisticas/adicionar_substituicao.html', {'form': form, 'jogo': jogo})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)





def editar_substituicao(request, id):
    try:
        substituicao = get_object_or_404(P_Substituicao, _id=ObjectId(id))  # Fixed model name
        jogo = substituicao.jogo
        if request.method == 'POST':
            form = P_SubstituicaoForm(request.POST, instance=substituicao, jogo=jogo)
            if form.is_valid():
                form.save()
                return redirect('listar_estatisticas', id=str(jogo._id))
            else:
                return JsonResponse({'error': form.errors}, status=400)
        form = P_SubstituicaoForm(instance=substituicao, jogo=jogo)
        return render(request, 'estatisticas/editar_substituicao.html', {
            'form': form, 
            'substituicao': substituicao, 
            'jogo': jogo
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
        
        
        
        
        
def apagar_substituicao(request, id):
    try:
        if request.method == 'POST':
            substituicao = get_object_or_404(P_Substituicao, _id=ObjectId(id))
            substituicao.delete()
            return redirect('listar_estatisticas', id=substituicao.jogo.get_id())
        else:
            return JsonResponse({'error': 'Método não permitido'}, status=405)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

    
    
    
    
# --- Clubes Favoritos ---
@login_required
def favorito_clube(request, clube_id):
    clube = get_object_or_404(P_Clube, _id=ObjectId(clube_id))
    utilizador = request.user  # O utilizador logado

    # Verifica se o clube já está nos favoritos
    favorito, created = P_ClubeFavorito.objects.get_or_create(utilizador_id=utilizador.utilizador_id, clube=clube)

    if not created:  # Se já existia um favorito, removemos
        favorito.delete()
        action = 'removido'
    else:
        action = 'adicionado'
    
    return redirect('detalhes_clube', id=clube.get_id())
    
    
    
    
def remover_favorito(request, clube_id):
    clube = get_object_or_404(P_Clube, _id=ObjectId(clube_id))
    utilizador = request.user  # O utilizador logado

    # Verifica se o clube está nos favoritos do utilizador
    favorito = P_ClubeFavorito.objects.filter(utilizador_id=utilizador.utilizador_id, clube=clube).first()

    if favorito:  # Se existir um favorito, removemos
        favorito.delete()

    return redirect('perfil')




# --- OUTROS ---
def get_equipas_por_clube(request, clube_id):
    try:
        print(f"Recebida requisição para clube_id: {clube_id}")  # Debug
        clube = P_Clube.objects.get(_id=ObjectId(clube_id))
        print(f"Clube encontrado: {clube.nome}")  # Debug
        
        # Filtrar apenas equipas ativas do clube
        equipas = P_Equipa.objects.filter(clube=clube, estado="Ativa")
        print(f"Equipas encontradas: {equipas.count()}")  # Debug
        
        data = [{
            'id': str(equipa._id),
            'nome': equipa.nome
        } for equipa in equipas]
        
        print(f"Dados retornados: {data}")  # Debug
        return JsonResponse(data, safe=False)
    except Exception as e:
        print(f"Erro: {str(e)}")  # Debug
        return JsonResponse({'error': str(e)}, status=400)
      


      
def get_jogadores_por_clube(request):
    clube_id = request.GET.get('clube_id')
    jogo_id = request.GET.get('jogo_id')
    
    if clube_id and jogo_id:
        try:
            jogo = P_Jogo.objects.get(_id=ObjectId(jogo_id))
            clube = P_Clube.objects.get(_id=ObjectId(clube_id))
            
            # Debug prints
            print(f"Clube Casa ID: {jogo.clube_casa._id if jogo.clube_casa else 'None'}")
            print(f"Clube Fora ID: {jogo.clube_fora._id if jogo.clube_fora else 'None'}")
            print(f"Selected Clube ID: {clube._id if clube else 'None'}")
            print(f"Equipa Casa: {jogo.equipa_casa._id if jogo.equipa_casa else 'None'}")
            print(f"Equipa Fora: {jogo.equipa_fora._id if jogo.equipa_fora else 'None'}")
            
            # Adiciona validações
            if not jogo.clube_casa or not jogo.clube_fora:
                return JsonResponse({'error': 'Jogo não tem clubes definidos'}, status=400)
                
            if not jogo.equipa_casa or not jogo.equipa_fora:
                return JsonResponse({'error': 'Jogo não tem equipas definidas'}, status=400)
            
            # Determina qual equipa baseado no clube selecionado com validação extra
            equipa = None
            if clube._id == jogo.clube_casa._id:
                equipa = jogo.equipa_casa
            elif clube._id == jogo.clube_fora._id:
                equipa = jogo.equipa_fora
                
            if not equipa:
                return JsonResponse({'error': 'Não foi possível determinar a equipa'}, status=400)
                
            players = P_Jogador.objects.filter(equipa=equipa)
            
            return JsonResponse({
                'players': [{'id': str(player._id), 'name': player.nome} for player in players]
            })
        except P_Jogo.DoesNotExist:
            return JsonResponse({'error': 'Jogo não encontrado'}, status=400)
        except P_Clube.DoesNotExist:
            return JsonResponse({'error': 'Clube não encontrado'}, status=400)
        except Exception as e:
            return JsonResponse({'error': f'Erro inesperado: {str(e)}'}, status=400)
            
    return JsonResponse({'error': 'Parâmetros obrigatórios faltando'}, status=400)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    