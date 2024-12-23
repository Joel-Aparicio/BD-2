from django import forms
from .models import Clube, Competicao, Jogo, FormatoCompeticao, PosicaoJogador, Jogador, Equipa, AssociacaoFutebol
from .models import P_Posicao, P_Associacao, P_FormatoCompeticao, P_Estadio, P_Jogador, P_Clube, P_Equipa


class P_PosicaoForm(forms.ModelForm):
    class Meta:
        model = P_Posicao
        fields = ['nome', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome da posição'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Digite a descrição'}),
        }
        labels = {
            'nome': 'Nome da Posição',
            'descricao': 'Descrição',
        }
        
class P_AssociacaoForm(forms.ModelForm):
    class Meta:
        model = P_Associacao
        fields = ['nome', 'url', 'pais', 'imagem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o nome da Associação'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o link da Associação'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o nome do País'}),
            'imagem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o url da imagem'}),
        }
        labels = {
            'nome': 'Nome da Associação',
            'url': 'Url da Associação (Opcional)',
            'pais': 'País',
            'imagem': 'Url da Imagem (Opcional)',
        }
        
    def clean(self):
        cleaned_data = super().clean()
        # Convert empty strings to None for URLFields
        if 'url' in cleaned_data and cleaned_data['url'] == '':
            cleaned_data['url'] = None
        if 'imagem' in cleaned_data and cleaned_data['imagem'] == '':
            cleaned_data['imagem'] = None
        return cleaned_data
        
class P_FormatoCompeticaoForm(forms.ModelForm):
    class Meta:
        model = P_FormatoCompeticao
        fields = ['nome', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o nome do Formato da Competição'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva a descrição'}),
        }
        labels = {
            'nome': 'Nome do Formato da Competição',
            'descricao': 'Descrição',
        }

class P_EstadioForm(forms.ModelForm):
    class Meta:
        model = P_Estadio
        fields = ['nome', 'pais', 'cidade', 'inauguracao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o nome do Estádio'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o país'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva a cidade'}),
            'inauguracao': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ano de Inauguração', 'min': 0}),
        }
        labels = {
            'nome': 'Nome do Estádio',
            'pais': 'País',
            'cidade': 'Cidade',
            'inauguracao': 'Ano de Inauguração'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['inauguracao'].initial = 1900  # Define o valor padrão para o formulário

class P_JogadorForm(forms.ModelForm):
    class Meta:
        model = P_Jogador
        fields = ['nome', 'idade', 'imagem', 'altura', 'peso', 'nacionalidade', 'num_camisola', 'valor_de_mercado', 'num_jogos', 'num_golos', 'situacao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o nome do Jogador'}),
            'idade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Idade', 'min': 0}),
            'imagem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o url da imagem'}),
            'altura': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Altura em centímetros', 'min': 0}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Peso do Jogador', 'min': 0}), #FLOAT
            'nacionalidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva a nacionalidade'}),
            'num_camisola': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número do Jogador', 'min': 1}),
            'valor_de_mercado': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor de Mercado', 'min': 0}),
            'num_jogos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de Jogos', 'min': 0}),    
            'num_golos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de Golos', 'min': 0}),    
            'situacao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Situação atual'}),
        }
        labels = {
            'nome': 'Nome do Jogador',
            'idade': 'Idade',
            'imagem': 'Imagem do Jogador',
            'altura': 'Altura (em cm)',
            'peso': 'Peso (em kg)',
            'nacionalidade': 'Nacionalidade',
            'num_camisola': 'Número Camisola',
            'valor_de_mercado': 'Valor de Mercado (em milhões)',
            'num_jogos': 'Número de Jogos',
            'num_golos': 'Número de Golos',
            'situacao': 'Situação'
        }
    
    def __init__(self, *args, **kwargs): # Define o valor padrão para o formulário
        super().__init__(*args, **kwargs)
        self.fields['peso'].initial = 60.0  
        self.fields['num_camisola'].initial = 0 
        self.fields['valor_de_mercado'].initial = 0.0
        self.fields['num_jogos'].initial = 0 
        self.fields['num_golos'].initial = 0  
        self.fields['situacao'].initial = 'Ativo'
    
    def clean(self):
        cleaned_data = super().clean()
        # Converte Strings vazias em None para campos URL
        if 'imagem' in cleaned_data and cleaned_data['imagem'] == '':
            cleaned_data['imagem'] = None
        return cleaned_data

class P_ClubeForm(forms.ModelForm):
    class Meta:
        model = P_Clube
        fields = ['nome', 'imagem', 'ano_fundacao', 'alcunhas', 'pais', 'cidade', 'extinto']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o nome do Clube'}),
            'imagem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o url da imagem'}),
            'ano_fundacao': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Fundação', 'min': 0}),
            'alcunhas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira as alcunhas'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o país'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva a cidade'}),         
            'extinto': forms.CheckboxInput(attrs={'class': 'form-check-input'})  # Adiciona o checkbox para o campo 'extinto'
        }
        labels = {
            'nome': 'Nome do Clube',
            'imagem': 'Imagem do Clube',
            'ano_fundacao': 'Ano Fundado',
            'alcunhas': 'Alcunhas',
            'pais': 'País',
            'cidade': 'Cidade',
            'extinto': 'Extinto?'  # Label do campo 'extinto'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ano_fundacao'].initial = 1900  # Define o valor padrão para 'ano_fundacao'
        self.fields['extinto'].initial = False  # Define o valor padrão para 'extinto' como False (não extinto)
    
    def clean(self):
        cleaned_data = super().clean()
        # Converte Strings vazias em None para campos URL
        if 'imagem' in cleaned_data and cleaned_data['imagem'] == '':
            cleaned_data['imagem'] = None
        return cleaned_data
        
        
class P_EquipaForm(forms.ModelForm):
    clube = forms.ModelChoiceField(
        queryset=P_Clube.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Escolha o clube",
    )

    class Meta:
        model = P_Equipa
        fields = ['clube', 'nome', 'ativa']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o nome da Equipa'}),
            'ativa': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'nome': 'Nome da Equipa',
            'ativa': 'Equipa Ativa',
        }
    
# --- TEMP ---
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
        model = P_Posicao
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

