from django import forms
from .models import Clube, Competicao, Jogo, FormatoCompeticao, PosicaoJogador, Jogador, Equipa, AssociacaoFutebol

class AssociacaoFutebolForm(forms.ModelForm):
    class Meta:
        model = AssociacaoFutebol
        fields = ['nome', 'pais', 'url']
        labels = {
            'nome': 'Nome',
            'pais': 'País',
            'url': 'Website',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome da associação'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o país'}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Digite a URL do site'}),
        }

class ClubeForm(forms.ModelForm):
    class Meta:
        model = Clube
        fields = ['nome', 'estadio', 'ano_fundacao', 'alcunha', 'pais', 'cidade']

class CompeticaoForm(forms.ModelForm):
    class Meta:
        model = Competicao
        fields = ['nome', 'descricao', 'ano', 'formato_competicao']  # Incluído o novo campo

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['descricao'].widget.attrs.update({'class': 'form-control', 'rows': 4})
        self.fields['ano'].widget.attrs.update({'class': 'form-control'})
        self.fields['formato_competicao'].widget.attrs.update({'class': 'form-control'})  # Estilo do campo


class JogoForm(forms.ModelForm):
    dia = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Data do Jogo"
    )
    hora = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        label="Hora do Jogo"
    )
    terminado = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(),
        label="Jogo Terminado"
    )

    class Meta:
        model = Jogo
        fields = ['ano', 'dia', 'hora', 'clube_casa', 'clube_fora', 'competicao', 'terminado']

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
        fields = ['nome', 'descricao']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['descricao'].widget.attrs.update({'class': 'form-control'})

class JogadorForm(forms.ModelForm):
    class Meta:
        model = Jogador
        fields = ['nome', 'nacionalidade', 'situacao', 'idade', 'num_camisola', 'posicao']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['nacionalidade'].widget.attrs.update({'class': 'form-control'})
        self.fields['situacao'].widget.attrs.update({'class': 'form-control'})
        self.fields['idade'].widget.attrs.update({'class': 'form-control', 'type': 'number', 'min': '0'})
        self.fields['num_camisola'].widget.attrs.update({'class': 'form-control', 'type': 'number', 'min': '0'})
        self.fields['posicao'].widget.attrs.update({'class': 'form-control'})
        
class EquipaForm(forms.ModelForm):
    class Meta:
        model = Equipa
        fields = ['nome', 'ativo', 'clube']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['ativo'].widget.attrs.update({'class': 'form-check-input'})  # Checkbox estilizado
        self.fields['clube'].widget.attrs.update({'class': 'form-control'})

