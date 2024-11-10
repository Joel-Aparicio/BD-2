from django import forms
from .models import Clube,Competicao

class ClubeForm(forms.ModelForm):
    class Meta:
        model = Clube
        fields = ['nome', 'estadio', 'ano_fundacao', 'alcunha']

class CompeticaoForm(forms.ModelForm):
    class Meta:
        model = Competicao
        fields = ['nome', 'descricao', 'ano']