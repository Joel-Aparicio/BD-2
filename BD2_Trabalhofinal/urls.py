"""
URL configuration for BD2_Trabalhofinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .App import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bd/conectividade', views.lista_utilizadores, name='lista_utilizadores'),
    path('login/', views.login, name='login'), 
    path('register/', views.register, name='register'),
    
    #Clubes
    path('admin/clubes/', views.lista_clubes, name='lista_clubes'),
    path('admin/clubes/adicionar/', views.adicionar_clube, name='adicionar_clube'),
    path('admin/clubes/<int:pk>/editar/', views.editar_clube, name='editar_clube'),
    path('admin/clubes/<int:pk>/deletar/', views.deletar_clube, name='deletar_clube'),
    path('clubes/<int:pk>/', views.detalhes_clube, name='detalhes_clube'),
    path('clubes/', views.todos_clubes, name='todos_clubes'),
    
    #Competições
    path('admin/competicoes/', views.lista_competicoes, name='lista_competicoes'),
    path('admin/competicoes/adicionar/', views.adicionar_competicao, name='adicionar_competicao'),
    path('admin/competicoes/<int:pk>/editar/', views.editar_competicao, name='editar_competicao'),
    path('admin/competicoes/<int:pk>/deletar/', views.deletar_competicao, name='deletar_competicao'),
    path('competicoes/<int:pk>/', views.detalhes_competicao, name='detalhes_competicao'),
    path('competicoes/', views.todos_competicoes, name='todos_competicoes'),
    
    #Jogos
    path('admin/jogos/', views.lista_jogos, name='lista_jogos'),
    path('admin/jogos/adicionar/', views.adicionar_jogo, name='adicionar_jogo'),
    path('admin/jogos/<int:pk>/editar/', views.editar_jogo, name='editar_jogo'),
    path('admin/jogos/<int:pk>/deletar/', views.deletar_jogo, name='deletar_jogo'),
    path('jogos/<int:pk>/', views.detalhes_jogo, name='detalhes_jogo'),
    path('jogos/', views.todos_jogos, name='todos_jogos'),
    
    # Formatos de Competição
    path('admin/formatoCompeticao/', views.lista_formatoCompeticao, name='lista_formatoCompeticao'),
    path('admin/formatoCompeticao/adicionar/', views.adicionar_formatoCompeticao, name='adicionar_formatoCompeticao'),
    path('admin/formatoCompeticao/<int:pk>/editar/', views.editar_formatoCompeticao, name='editar_formatoCompeticao'),
    path('admin/formatoCompeticao/<int:pk>/deletar/', views.deletar_formatoCompeticao, name='deletar_formatoCompeticao'),
    
    # Posições de Jogador
    path('admin/posicoesJogador/', views.lista_posicaoJogador, name='lista_posicaoJogador'),
    path('admin/posicoesJogador/adicionar/', views.adicionar_posicaoJogador, name='adicionar_posicaoJogador'),
    path('admin/posicoesJogador/<int:pk>/editar/', views.editar_posicaoJogador, name='editar_posicaoJogador'),
    path('admin/posicoesJogador/<int:pk>/deletar/', views.deletar_posicaoJogador, name='deletar_posicaoJogador'),
    
    #Jogadores
    path('admin/jogadores/', views.lista_jogadores, name='lista_jogadores'),
    path('admin/jogadores/adicionar/', views.adicionar_jogador, name='adicionar_jogador'),
    path('admin/jogadores/<int:pk>/editar/', views.editar_jogador, name='editar_jogador'),
    path('admin/jogadores/<int:pk>/deletar/', views.deletar_jogador, name='deletar_jogador'),
    path('jogadores/<int:pk>/', views.detalhes_jogador, name='detalhes_jogador'),
    path('jogadores/', views.todos_jogadores, name='todos_jogadores'),
    
    # Equipas
    path('admin/equipas/', views.lista_equipas, name='lista_equipas'),
    path('admin/equipas/adicionar/', views.adicionar_equipa, name='adicionar_equipa'),
    path('admin/equipas/<int:pk>/editar/', views.editar_equipa, name='editar_equipa'),
    path('admin/equipas/<int:pk>/deletar/', views.deletar_equipa, name='deletar_equipa'),
    
    #Associações de Futebol
    path('admin/associacaoFutebol/', views.lista_associacaoFutebol, name='lista_associacaoFutebol'),
    path('associacaoFutebol/<int:pk>/', views.detalhes_associacaoFutebol, name='detalhes_associacaoFutebol'),
    path('admin/associacaoFutebol/adicionar/', views.adicionar_associacaoFutebol, name='adicionar_associacaoFutebol'),
    path('admin/associacaoFutebol/editar/<int:pk>/', views.editar_associacaoFutebol, name='editar_associacaoFutebol'),
    path('admin/associacaoFutebol/<int:pk>/deletar/', views.deletar_associacaoFutebol, name='deletar_associacaoFutebol'),
    path('associacaoFutebol/', views.todos_associacaoFutebol, name='todos_associacaoFutebol'),
    
    

]

