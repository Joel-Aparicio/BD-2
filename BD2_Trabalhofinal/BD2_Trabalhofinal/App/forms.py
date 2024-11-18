from django import forms
from .models import Clube, Competicao, Jogo, FormatoCompeticao, PosicaoJogador

class ClubeForm(forms.ModelForm):
    class Meta:
        model = Clube
        fields = ['nome', 'estadio', 'ano_fundacao', 'alcunha', 'pais', 'cidade']

class CompeticaoForm(forms.ModelForm):
    class Meta:
        model = Competicao
        fields = ['nome', 'descricao', 'ano']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['descricao'].widget.attrs.update({'class': 'form-control', 'rows': 4})
        self.fields['ano'].widget.attrs.update({'class': 'form-control'})

class JogoForm(forms.ModelForm):
    dia = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Data do Jogo"
    )
    hora = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        label="Hora do Jogo"
    )

    class Meta:
        model = Jogo
        fields = ['ano', 'dia', 'hora', 'clube_casa', 'clube_fora', 'competicao']

    def clean(self):
        cleaned_data = super().clean()
        clube_casa = cleaned_data.get("clube_casa")
        clube_fora = cleaned_data.get("clube_fora")

        if clube_casa == clube_fora:
            raise forms.ValidationError("O clube casa e o clube fora não podem ser o mesmo.")
        
        return cleaned_data

#Formato da Competição
class FormatoCompeticaoForm(forms.ModelForm):
    class Meta:
        model = FormatoCompeticao
        fields = ['nome', 'descricao']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['descricao'].widget.attrs.update({'class': 'form-control', 'rows': 4})

#Posicao do Jogador
class PosicaoJogadorForm(forms.ModelForm):
    class Meta:
        model = PosicaoJogador
        fields = ['nome']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
