from django.core.exceptions import ValidationError
from bson import ObjectId
from .models import P_Clube, P_Jogador, P_Posicao, P_Associacao, P_Estadio, P_Equipa, P_FormatoCompeticao, P_Competicao

# Estas funções servem para o forms.py
# Têm o objetivo de converter as chaves estrangeiras num ObjectId


def convert_to_clube(value):
    if not value:
        return None
    try:
        if isinstance(value, str):
            return P_Clube.objects.get(_id=ObjectId(value))
        return value
    except Exception as e:
        raise ValidationError('Clube inválido')



def convert_to_jogador(value):
    if not value:
        return None
    try:
        if isinstance(value, str):
            return P_Jogador.objects.get(_id=ObjectId(value))
        return value
    except Exception as e:
        raise ValidationError('Jogador inválido')



def convert_to_posicao(value):
    if not value:
        return None
    try:
        if isinstance(value, str):
            return P_Posicao.objects.get(_id=ObjectId(value))
        return value
    except Exception as e:
        raise ValidationError('Posição inválida')



def convert_to_associacao(value):
    if not value:
        return None
    try:
        if isinstance(value, str):
            return P_Associacao.objects.get(_id=ObjectId(value))
        return value
    except Exception as e:
        raise ValidationError('Associação inválida')



def convert_to_estadio(value):
    if not value:
        return None
    try:
        if isinstance(value, str):
            return P_Estadio.objects.get(_id=ObjectId(value))
        return value
    except Exception as e:
        raise ValidationError('Estádio inválido')



def convert_to_equipa(value):
    if not value:
        return None
    try:
        if isinstance(value, str):
            return P_Equipa.objects.get(_id=ObjectId(value))
        return value
    except Exception as e:
        raise ValidationError('Equipa inválida')



def convert_to_formato(value):
    if not value:
        return None
    try:
        if isinstance(value, str):
            return P_FormatoCompeticao.objects.get(_id=ObjectId(value))
        return value
    except Exception as e:
        raise ValidationError('Formato inválido')



def convert_to_competicao(value):
    if not value:
        return None
    try:
        if isinstance(value, str):
            return P_Competicao.objects.get(_id=ObjectId(value))
        return value
    except Exception as e:
        raise ValidationError('Competição inválida')
        
        
        
        