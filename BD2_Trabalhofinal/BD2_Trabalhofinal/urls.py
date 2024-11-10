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
    path('clubes/', views.lista_clubes, name='lista_clubes'),
    path('clubes/adicionar/', views.adicionar_clube, name='adicionar_clube'),
    path('clubes/<int:pk>/editar/', views.editar_clube, name='editar_clube'),
    path('clubes/<int:pk>/deletar/', views.deletar_clube, name='deletar_clube'),
    path('clubes/<int:pk>/', views.detalhes_clube, name='detalhes_clube'),
    path('competicoes/', views.lista_competicoes, name='lista_competicoes'),
    path('competicoes/adicionar/', views.adicionar_competicao, name='adicionar_competicao'),
    path('competicoes/<int:pk>/editar/', views.editar_competicao, name='editar_competicao'),
    path('competicoes/<int:pk>/deletar/', views.deletar_competicao, name='deletar_competicao'),
    path('competicoes/<int:pk>/', views.detalhes_competicao, name='detalhes_competicao'),

]

