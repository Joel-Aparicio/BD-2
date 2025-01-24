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
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    
    # POSIÇÕES DE CAMPO DOS JOGADORES
    path('admin/posicoes/', views.listar_posicoes, name='listar_posicoes'),
    path('admin/posicoes/adicionar/', views.adicionar_posicao, name='adicionar_posicao'),
    path('admin/posicoes/editar/<str:id>/', views.editar_posicao, name='editar_posicao'),
    path('admin/posicoes/apagar/<str:id>/', views.apagar_posicao, name='apagar_posicao'),
    
    # ASSOCIAÇÕES DE FUTEBOL
    path('admin/associacoes/', views.listar_associacoes, name='listar_associacoes'),
    path('admin/associacoes/adicionar/', views.adicionar_associacao, name='adicionar_associacao'),
    path('admin/associacoes/editar/<str:id>/', views.editar_associacao, name='editar_associacao'),
    path('admin/associacoes/apagar/<str:id>/', views.apagar_associacao, name='apagar_associacao'),
    path('associacoes/', views.todas_associacoes, name='todas_associacoes'),
    path('associacoes/<str:id>/', views.detalhes_associacao, name='detalhes_associacao'),
    
    # FORMATOS DE COMPETIÇÃO
    path('admin/formatos/', views.listar_formatos, name='listar_formatos'),
    path('admin/formatos/adicionar/', views.adicionar_formato, name='adicionar_formato'),
    path('admin/formatos/editar/<str:id>/', views.editar_formato, name='editar_formato'),
    path('admin/formatos/apagar/<str:id>/', views.apagar_formato, name='apagar_formato'),
    
    # ESTÁDIOS
    path('admin/estadios/', views.listar_estadios, name='listar_estadios'),
    path('admin/estadios/adicionar/', views.adicionar_estadio, name='adicionar_estadio'),
    path('admin/estadios/editar/<str:id>/', views.editar_estadio, name='editar_estadio'),
    path('admin/estadios/apagar/<str:id>/', views.apagar_estadio, name='apagar_estadio'),
    path('estadios/', views.todos_estadios, name='todos_estadios'),
    path('estadios/<str:id>/', views.detalhes_estadio, name='detalhes_estadio'),
    
    # JOGADORES
    path('admin/jogadores/', views.listar_jogadores, name='listar_jogadores'),
    path('admin/jogadores/adicionar/', views.adicionar_jogador, name='adicionar_jogador'),
    path('admin/jogadores/editar/<str:id>/', views.editar_jogador, name='editar_jogador'),
    path('admin/jogadores/apagar/<str:id>/', views.apagar_jogador, name='apagar_jogador'),
    path('jogadores/', views.todos_jogadores, name='todos_jogadores'),
    path('jogadores/<str:id>/', views.detalhes_jogador, name='detalhes_jogador'),

    # CLUBES  
    path('admin/clubes/', views.listar_clubes, name='listar_clubes'),
    path('admin/clubes/adicionar/', views.adicionar_clube, name='adicionar_clube'),
    path('admin/clubes/editar/<str:id>/', views.editar_clube, name='editar_clube'),
    path('admin/clubes/apagar/<str:id>/', views.apagar_clube, name='apagar_clube'),
    path('clubes/', views.todos_clubes, name='todos_clubes'),
    path('clubes/<str:id>/', views.detalhes_clube, name='detalhes_clube'),
    
    # EQUIPAS
    path('admin/equipas/', views.listar_equipas, name='listar_equipas'),
    path('admin/equipas/adicionar/', views.adicionar_equipa, name='adicionar_equipa'),
    path('admin/equipas/editar/<str:id>/', views.editar_equipa, name='editar_equipa'),
    path('admin/equipas/apagar/<str:id>/', views.apagar_equipa, name='apagar_equipa'),
    
    # EQUIPAS - CLUBES
    path('api/equipas-por-clube/<str:clube_id>/', views.get_equipas_por_clube, name='equipas_por_clube'),
    
    # COMPETIÇÕES
    path('admin/competicoes/', views.listar_competicoes, name='listar_competicoes'),
    path('admin/competicoes/adicionar/', views.adicionar_competicao, name='adicionar_competicao'),
    path('admin/competicoes/editar/<str:id>/', views.editar_competicao, name='editar_competicao'),
    path('admin/competicoes/apagar/<str:id>/', views.apagar_competicao, name='apagar_competicao'),
    path('competicoes/<str:id>/', views.detalhes_competicao, name='detalhes_competicao'),
    path('competicoes/', views.todas_competicoes, name='todas_competicoes'),
    
    # JOGOS
    path('admin/jogos/', views.listar_jogos, name='listar_jogos'),
    path('admin/jogos/adicionar/', views.adicionar_jogo, name='adicionar_jogo'),    
    path('admin/jogos/editar/<str:id>/', views.editar_jogo, name='editar_jogo'),
    path('admin/jogos/apagar/<str:id>/', views.apagar_jogo, name='apagar_jogo'),
    path('jogos/<str:id>/', views.detalhes_jogo, name='detalhes_jogo'),
    path('jogos/', views.todos_jogos, name='todos_jogos'),
    
    # ESTATISTICAS JOGOS
    path('admin/jogos/estatisticas/<str:id>/', views.listar_estatisticas, name='listar_estatisticas'),

]

