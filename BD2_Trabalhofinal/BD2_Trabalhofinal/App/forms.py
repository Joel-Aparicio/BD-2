from django import forms
from django.core.exceptions import ValidationError
from bson import ObjectId  # Adicione esta importação!
from .models import P_Posicao, P_Associacao, P_FormatoCompeticao, P_Estadio, P_Jogador, P_Clube, P_Equipa, P_Competicao, P_Jogo
from .models import P_Golo, P_Penalti, P_Falta, P_Substituicao
from .models import Utilizador
from django.contrib.auth.forms import PasswordChangeForm
from .form_utils import convert_to_clube, convert_to_equipa, convert_to_posicao, convert_to_jogador, convert_to_associacao, convert_to_formato, convert_to_competicao, convert_to_estadio

# --- Utilizador ---
class P_PerfilForm(forms.ModelForm):
    class Meta:
        model = Utilizador
        fields = ['nome', 'email']  # Campos que podem ser editados
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }
        labels = {
            'nome': 'Nome',
            'email': 'Email',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Utilizador.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso por outro utilizador.")
        return email
               
class P_SenhaForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Senha Atual",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Digite sua senha atual"}),
    )
    new_password1 = forms.CharField(
        label="Nova Senha",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Digite sua nova senha"}),
    )
    new_password2 = forms.CharField(
        label="Confirme a Nova Senha",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirme sua nova senha"}),
    )


# --- Website ---
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
        fields = ['nome', 'descricao', 'valor_de_mercado']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o nome do Formato da Competição'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva a descrição'}),
            'valor_de_mercado': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor de Mercado', 'min': 0}),
        }
        labels = {
            'nome': 'Nome do Formato da Competição',
            'descricao': 'Descrição',
            'valor_de_mercado': 'Valor de Mercado (em milhões)'
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['valor_de_mercado'].initial = 0.0

class P_EstadioForm(forms.ModelForm):
    estado = forms.ChoiceField(
        choices=[
            ('', 'Selecione a Situação'),
            ('Ativo', 'Ativo'),
            ('Em Obras', 'Em Obras'),
            ('Demolido', 'Demolido'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    
    class Meta:
        model = P_Estadio
        fields = ['nome', 'imagem', 'pais', 'cidade', 'inauguracao', 'lotacao', 'estado']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o nome do Estádio'}),
            'imagem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o url da imagem'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o país'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva a cidade'}),
            'inauguracao': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ano de Inauguração', 'min': 0}),
            'lotacao': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Lotacao', 'min': 0}),
        }
        labels = {
            'nome': 'Nome do Estádio',
            'imagem': 'Imagem do Estádio',
            'pais': 'País',
            'cidade': 'Cidade',
            'inauguracao': 'Ano de Inauguração',
            'lotacao': 'Lotação do Estádio',
            'estado': 'Estado'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['inauguracao'].initial = 1900  # Define o valor padrão para o formulário
        
    def clean(self):
        cleaned_data = super().clean()
        # Converte Strings vazias em None para campos URL
        if 'imagem' in cleaned_data and cleaned_data['imagem'] == '':
            cleaned_data['imagem'] = None
        return cleaned_data
        

class P_JogadorForm(forms.ModelForm):
   clube = forms.ModelChoiceField(
       queryset=P_Clube.objects.all(),
       widget=forms.Select(attrs={'class': 'form-control'}),
       empty_label="Escolha o clube (opcional)",
       required=False
   )
   
   equipa = forms.ModelChoiceField(
       queryset=P_Equipa.objects.none(),  # Começa vazio
       widget=forms.Select(attrs={'class': 'form-control'}),
       empty_label="Escolha a equipa (opcional)",
       required=False
   )
   
   posicao = forms.ModelChoiceField(
       queryset=P_Posicao.objects.all(),
       widget=forms.Select(attrs={'class': 'form-control'}),
       empty_label="Escolha a posição"
   )
    
   situacao = forms.ChoiceField(
        choices=[
            ('', 'Selecione a Situação'),
            ('Ativo', 'Ativo'),
            ('Aleijado', 'Aleijado'),
            ('Expulso', 'Expulso'),
            ('Sem Clube', 'Sem Clube'),
            ('Reformado', 'Reformado'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    
   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)       
       # Configurações existentes
       self.fields['peso'].initial = 60.0
       self.fields['num_camisola'].initial = 0
       self.fields['valor_de_mercado'].initial = 0.0
       self.fields['situacao'].initial = 'Ativo'
       self.fields['altura'].initial = 0
       self.fields['idade'].initial = 0
       
       # Configurar label_from_instance para clube, posição e equipa
       self.fields['clube'].label_from_instance = lambda obj: f"{obj.nome}"
       self.fields['equipa'].label_from_instance = lambda obj: f"{obj.nome}"
       self.fields['posicao'].label_from_instance = lambda obj: f"{obj.nome} ({obj.descricao})" if obj.descricao else f"{obj.nome}"
       
       # Configurar to_python para clube, posição e equipa
       self.fields['clube'].to_python = convert_to_clube
       self.fields['equipa'].to_python = convert_to_equipa
       self.fields['posicao'].to_python = convert_to_posicao

       # Se estiver editando um jogador existente
       if 'instance' in kwargs and kwargs['instance']:
           jogador = kwargs['instance']
           if jogador.clube:
               # Filtra as equipas do clube selecionado
               self.fields['equipa'].queryset = P_Equipa.objects.filter(clube=jogador.clube)

   def clean(self):
       cleaned_data = super().clean()
       # Converte Strings vazias em None para campos URL
       if 'imagem' in cleaned_data and cleaned_data['imagem'] == '':
           cleaned_data['imagem'] = None
       return cleaned_data

   class Meta:
       model = P_Jogador
       fields = ['nome', 'idade', 'imagem', 'altura', 'peso', 'nacionalidade', 
                'num_camisola', 'valor_de_mercado', 'situacao', 'posicao', 'clube', 'equipa']
       widgets = {
           'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o nome do Jogador'}),
           'idade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Idade', 'min': 0}),
           'imagem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o url da imagem'}),
           'altura': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Altura em centímetros', 'min': 0}),
           'peso': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Peso do Jogador', 'min': 0}),
           'nacionalidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva a nacionalidade'}),
           'num_camisola': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número do Jogador', 'min': 1}),
           'valor_de_mercado': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor de Mercado', 'min': 0}), 
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
           'situacao': 'Situação',
           'posicao': 'Posição do Jogador',
           'clube': 'Clube (opcional)',
           'equipa': 'Equipa (opcional)'
       }

class P_ClubeForm(forms.ModelForm):
    associacao = forms.ModelChoiceField(
        queryset=P_Associacao.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False,
        empty_label="Selecione uma associação (opcional)"
    )
    estadio = forms.ModelChoiceField(
        queryset=P_Estadio.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False,
        empty_label="Selecione uma estádio (opcional)"
    )
    
    estado = forms.ChoiceField(
        choices=[
            ('', 'Selecione a Situação'),
            ('Ativo', 'Ativo'),
            ('Suspenso', 'Suspenso'),
            ('Extinto', 'Extinto'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ano_fundacao'].initial = 1900
        self.fields['ano_extinto'].initial = 0
        self.fields['associacao'].label_from_instance = lambda obj: f"{obj.nome} ({obj.pais})"
        # Adicionar o conversor para a associação e estadio
        self.fields['associacao'].to_python = convert_to_associacao
        self.fields['estadio'].to_python = convert_to_estadio

    class Meta:
        model = P_Clube
        fields = ['nome', 'imagem', 'ano_fundacao', 'estado', 'ano_extinto', 'alcunhas', 'pais', 'cidade', 'associacao', 'estadio']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o nome do Clube'}),
            'imagem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o url da imagem'}),
            'ano_fundacao': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Fundação', 'min': 0}),
            'ano_extinto': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Extinto', 'min': 0}),
            'alcunhas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira as alcunhas'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o país'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva a cidade'}),         
        }
        labels = {
            'nome': 'Nome do Clube',
            'imagem': 'Imagem do Clube',
            'ano_fundacao': 'Ano Fundado',
            'ano_extinto': 'Ano Extinto',
            'alcunhas': 'Alcunhas',
            'pais': 'País',
            'cidade': 'Cidade',
            'Estado': 'Estado do Clube',
            'associacao': 'Associação',
            'estadio': 'Estádio (Se existir)'
        }
    
    def clean(self):
        cleaned_data = super().clean()
        if 'imagem' in cleaned_data and cleaned_data['imagem'] == '':
            cleaned_data['imagem'] = None
            
        estado = cleaned_data.get('estado')
        ano_extinto = cleaned_data.get('ano_extinto')
        
        if estado == 'Extinto' and (not ano_extinto or ano_extinto == 0):
            raise forms.ValidationError('Para clubes extintos, é necessário informar o ano de extinção.')
        
        if estado != 'Extinto' and ano_extinto and ano_extinto != 0:
            cleaned_data['ano_extinto'] = 0
            
        return cleaned_data
        
        
class P_EquipaForm(forms.ModelForm):
    clube = forms.ModelChoiceField(
        queryset=P_Clube.objects.filter(estado="Ativo"),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Escolha o clube"
    )
    
    estado = forms.ChoiceField(
        choices=[
            ('', 'Selecione a Situação'),
            ('Ativa', 'Ativa'),
            ('Suspensa', 'Suspensa'),
            ('Extinta', 'Extinta'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        self.fields['clube'].label_from_instance = lambda obj: f"{obj.nome}"
        self.fields['clube'].to_python = convert_to_clube
        
    class Meta:
        model = P_Equipa
        fields = ['clube', 'nome', 'estado']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o nome da Equipa'}),
        }
        labels = {
            'nome': 'Nome da Equipa',
            'estado': 'Estado da Equipa',
        }
        

class P_CompeticaoForm(forms.ModelForm):
    formato = forms.ModelChoiceField(
        queryset=P_FormatoCompeticao.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Escolha o Formato"
    )

    # VENCEDOR
    vencedor = forms.ModelChoiceField(
        queryset=P_Clube.objects.none(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Sem Vencedor / Empate",
        required=False
    )

    data_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label="Data de Início"
    )

    data_fim = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label="Data de Fim"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['formato'].label_from_instance = lambda obj: f"{obj.nome}"
        self.fields['formato'].to_python = convert_to_formato
        self.fields['vencedor'].label_from_instance = lambda obj: f"{obj.nome}"
        self.fields['vencedor'].to_python = convert_to_clube

    def clean(self):
        cleaned_data = super().clean()
        # Converte Strings vazias em None para campos URL
        if 'imagem' in cleaned_data and cleaned_data['imagem'] == '':
            cleaned_data['imagem'] = None

        # Verifica se a competição está finalizada
        finalizado = cleaned_data.get('finalizado')
        vencedor = cleaned_data.get('vencedor')

        #if finalizado and not vencedor:
            #raise ValidationError('É necessário selecionar um clube vencedor quando a competição está finalizada.')

        # Se não estiver finalizada, o vencedor deve ser None
        if not finalizado:
            cleaned_data['vencedor'] = None

        return cleaned_data

    class Meta:
        model = P_Competicao
        fields = ['nome', 'imagem', 'formato', 'data_inicio', 'data_fim', 'finalizado', 'vencedor']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o nome da Competição'}),
            'imagem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o url da imagem'}),
            'finalizado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'nome': 'Nome da Competição',
            'imagem': 'URL da Imagem',
            'finalizado': 'Competição Finalizada'
        }
        
        
        
        
class P_JogoForm(forms.ModelForm):

    # VENCEDOR
    vencedor = forms.ModelChoiceField(
        queryset=P_Clube.objects.none(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Sem Vencedor / Empate",
        required=False
    )
    
    # CASA
    clube_casa = forms.ModelChoiceField(
        queryset=P_Clube.objects.filter(estado="Ativo"),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Escolha o Clube Casa"
    )
    equipa_casa = forms.ModelChoiceField(
        queryset=P_Equipa.objects.filter(estado="Ativa"),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Escolha a Equipa Casa"
    )
    # FORA
    clube_fora = forms.ModelChoiceField(
        queryset=P_Clube.objects.filter(estado="Ativo"),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Escolha o Clube Fora"
    )
    equipa_fora = forms.ModelChoiceField(
        queryset=P_Equipa.objects.filter(estado="Ativa"),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Escolha a Equipa Fora"
    )
    
    
    # COMPETICAO E ESTADIO
    competicao = forms.ModelChoiceField(
        queryset=P_Competicao.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Escolha a Competicao"
    )
    estadio = forms.ModelChoiceField(
        queryset=P_Estadio.objects.filter(estado="Ativo"),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Escolha o Estádio"
    )
    
    # DIA e HORA
    dia = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label="Dia do Jogo"
    )
    hora = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                'type': 'time',
                'class': 'form-control'
            }
        ),
        label="Hora do Jogo"
    )
    
    estado = forms.ChoiceField(
        choices=[
            ('', 'Selecione o Estado'),
            ('Em Breve', 'Em Breve'),
            ('A Decorrer', 'A Decorrer'),
            ('Terminado', 'Terminado'),
            ('Cancelado', 'Cancelado'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )

    
    def clean(self):
        cleaned_data = super().clean()
        
        # Validar se os clubes são diferentes
        clube_casa = cleaned_data.get('clube_casa')
        clube_fora = cleaned_data.get('clube_fora')
        if clube_casa and clube_fora and clube_casa == clube_fora:
            raise ValidationError('Os clubes não podem ser iguais')
        
        # Validar campos obrigatórios com ObjectId
        required_fields = ['competicao', 'clube_casa', 'clube_fora', 'equipa_casa', 'equipa_fora', 'estadio']
        for field in required_fields:
            if not cleaned_data.get(field):
                self.add_error(field, f'Este campo é obrigatório')
        
        # Validar duração
        duracao = cleaned_data.get('duracao')
        if duracao and duracao < 90:
            self.add_error('duracao', 'A duração mínima deve ser 90 minutos')
        
        # Validar estado
        estado = cleaned_data.get('estado')
        if not estado:
            self.add_error('estado', 'Estado é obrigatório')
            
        # Validar dia
        dia = cleaned_data.get('dia')
        if not dia:
            self.add_error('dia', 'Dia é obrigatório')
        
        # Validar se o estádio está disponível naquele dia
        estadio = cleaned_data.get('estadio')
        if dia and estadio:
            # Procurar jogos no mesmo dia e no mesmo estádio
            jogos_mesmo_dia = P_Jogo.objects.filter(
                dia=dia,
                estadio=estadio
            )
            
            # Se estiver editando, excluir o jogo atual da verificação
            if self.instance and self.instance.pk:
                jogos_mesmo_dia = jogos_mesmo_dia.exclude(pk=self.instance.pk)
            
            if jogos_mesmo_dia.exists():
                raise ValidationError('Os clubes não podem ser iguais')
                self.add_error('estadio', 'Este estádio já tem um jogo marcado para este dia!')
            
        # Converter hora para string no formato HH:mm
        hora = cleaned_data.get('hora')
        if hora:
            cleaned_data['hora'] = hora.strftime('%H:%M')
        
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['duracao'].initial = 90
        
         # Inicialmente, não mostrar nenhuma equipa
        self.fields['equipa_casa'].queryset = P_Equipa.objects.none()
        self.fields['equipa_casa'].label_from_instance = lambda obj: f"{obj.nome} ({obj.clube.nome})"
        self.fields['equipa_casa'].to_python = convert_to_equipa
    
        # Inicialmente, não mostrar nenhuma equipa
        self.fields['equipa_fora'].queryset = P_Equipa.objects.none()
        self.fields['equipa_fora'].label_from_instance = lambda obj: f"{obj.nome} ({obj.clube.nome})"
        self.fields['equipa_fora'].to_python = convert_to_equipa
        
        # CASA
        self.fields['clube_casa'].label_from_instance = lambda obj: f"{obj.nome}"
        self.fields['clube_casa'].to_python = convert_to_clube
        self.fields['equipa_casa'].label_from_instance = lambda obj: f"{obj.nome} ({obj.clube.nome})"
        self.fields['equipa_casa'].to_python = convert_to_equipa
        # FORA
        self.fields['clube_fora'].label_from_instance = lambda obj: f"{obj.nome}"
        self.fields['clube_fora'].to_python = convert_to_clube
        self.fields['equipa_fora'].label_from_instance = lambda obj: f"{obj.nome} ({obj.clube.nome})"
        self.fields['equipa_fora'].to_python = convert_to_equipa
        
        # COMPETICAO
        self.fields['competicao'].label_from_instance = lambda obj: f"{obj.nome}"
        self.fields['competicao'].to_python = convert_to_competicao
        # ESTADIO
        self.fields['estadio'].label_from_instance = lambda obj: f"{obj.nome}"
        self.fields['estadio'].to_python = convert_to_estadio
        # VENCEDOR
        self.fields['vencedor'].label_from_instance = lambda obj: f"{obj.nome}"
        self.fields['vencedor'].to_python = convert_to_clube
        
        
        # Se estivermos "EDITAR" um jogo
        if self.instance and hasattr(self.instance, 'pk') and self.instance.pk:
            try:
                # Carregar equipas do clube casa =>  usa-se hasattr() para garantir que os atributos existem antes de tentar acessá-los
                if hasattr(self.instance, 'clube_casa') and self.instance.clube_casa:
                    self.fields['equipa_casa'].queryset = P_Equipa.objects.filter(clube=self.instance.clube_casa)
                
                # Carregar equipas do clube fora
                if hasattr(self.instance, 'clube_fora') and self.instance.clube_fora:
                    self.fields['equipa_fora'].queryset = P_Equipa.objects.filter(clube=self.instance.clube_fora)
            except Exception as e:
                # Se houver algum erro, mantenha os querysets vazios
                self.fields['equipa_casa'].queryset = P_Equipa.objects.none()
                self.fields['equipa_fora'].queryset = P_Equipa.objects.none()
                
        # Preencher o campo 'vencedor' apenas com os clubes do jogo (casa e fora)
        if self.instance and self.instance.pk:  # Verifica se é "EDITAR"
            clube_casa = getattr(self.instance, 'clube_casa', None)
            clube_fora = getattr(self.instance, 'clube_fora', None)

            if clube_casa and clube_fora:
                self.fields['vencedor'].queryset = P_Clube.objects.filter(pk__in=[clube_casa.pk, clube_fora.pk])
            else:
                self.fields['vencedor'].queryset = P_Clube.objects.none()
        else:  # No caso de "ADICIONAR", exibe todos os clubes
            self.fields['vencedor'].queryset = P_Clube.objects.all()

    class Meta:
        model = P_Jogo
        fields = ['dia', 'hora', 'competicao', 'estadio', 'clube_casa', 'equipa_casa', 'clube_fora', 'equipa_fora', 'estado', 'duracao', 'prolongamento', 'penaltis', 'vencedor']
        widgets = {
            'duracao': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Duração', 
                'min': 90,
                'required': 'required'
            }),
            'prolongamento': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'penaltis': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'estado': 'Estado do Jogo',
            'duracao': 'Duração do Jogo',
            'prolongamento': 'Houve Prolongamento?',
            'penaltis': 'Houve Penáltis?'
        }

# ESTATISTICAS
class P_GoloForm(forms.ModelForm):
    clube = forms.ModelChoiceField(
        queryset=P_Clube.objects.none(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'clube-select'
        }),
        empty_label="Escolha o clube"
    )
    jogador = forms.ModelChoiceField(
        queryset=P_Jogador.objects.none(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'jogador-select'
        }),
        empty_label="Escolha o jogador"
    )

    def __init__(self, *args, jogo=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['minuto'].initial = 0        
        self.fields['compensacao'].initial = 0     
        
        if jogo:
            # Verifica se os clubes existem
            if jogo.clube_casa and jogo.clube_fora:
                self.fields['clube'].queryset = P_Clube.objects.filter(
                    _id__in=[jogo.clube_casa._id, jogo.clube_fora._id]
                )
            
            # Se estivermos editando um golo existente
            if self.instance and self.instance.pk and self.instance.clube:
                equipa = None
                # Determina qual equipa baseado no clube
                if jogo.clube_casa and self.instance.clube._id == jogo.clube_casa._id:
                    equipa = jogo.equipa_casa
                elif jogo.clube_fora and self.instance.clube._id == jogo.clube_fora._id:
                    equipa = jogo.equipa_fora
                    
                if equipa:
                    self.fields['jogador'].queryset = P_Jogador.objects.filter(
                        equipa=equipa
                    )
        
        self.fields['clube'].label_from_instance = lambda obj: f"{obj.nome}"
        self.fields['clube'].to_python = convert_to_clube
        self.fields['jogador'].label_from_instance = lambda obj: f"{obj.nome}"
        self.fields['jogador'].to_python = convert_to_jogador
        
        self.jogo = jogo
        
    class Meta:
        model = P_Golo
        fields = ['clube', 'jogador', 'penalti', 'minuto', 'compensacao']
        widgets = {
            'minuto': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Duração', 
                'min': 0,
                'required': 'required'
            }),
            'compensacao': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Compensação', 
                'min': 0,
                'required': 'required'
            }),
            'penalti': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'minuto': 'Minuto do Golo',
            'compensacao': 'Compensação (Se existir)',
            'penalti': 'Penálti?'
        }
        
class P_PenaltiForm(forms.ModelForm):
    clube = forms.ModelChoiceField(
        queryset=P_Clube.objects.none(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'clube-select'
        }),
        empty_label="Escolha o clube"
    )
    jogador = forms.ModelChoiceField(
        queryset=P_Jogador.objects.none(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'jogador-select'
        }),
        empty_label="Escolha o jogador"
    )
    
    def __init__(self, *args, jogo=None, **kwargs):
        super().__init__(*args, **kwargs)    
        self.fields['numero'].initial = 0
        
        if jogo:
            # Verifica se os clubes existem
            if jogo.clube_casa and jogo.clube_fora:
                self.fields['clube'].queryset = P_Clube.objects.filter(
                    _id__in=[jogo.clube_casa._id, jogo.clube_fora._id]
                )
            
            # Se estivermos editando um penalti existente
            if self.instance and self.instance.pk and self.instance.clube:
                equipa = None
                # Determina qual equipa baseado no clube
                if jogo.clube_casa and self.instance.clube._id == jogo.clube_casa._id:
                    equipa = jogo.equipa_casa
                elif jogo.clube_fora and self.instance.clube._id == jogo.clube_fora._id:
                    equipa = jogo.equipa_fora
                    
                if equipa:
                    self.fields['jogador'].queryset = P_Jogador.objects.filter(
                        equipa=equipa
                    )
                    
        ## IDs
        self.fields['clube'].label_from_instance = lambda obj: f"{obj.nome}"
        self.fields['clube'].to_python = convert_to_clube
        self.fields['jogador'].label_from_instance = lambda obj: f"{obj.nome}"
        self.fields['jogador'].to_python = convert_to_jogador
        
        self.jogo = jogo
        
    class Meta:
        model = P_Penalti
        fields = ['numero', 'clube', 'jogador', 'golo']
        widgets = {
            'numero': forms.NumberInput(attrs={
                    'class': 'form-control', 
                    'placeholder': 'Duração', 
                    'min': 1,
                    'required': 'required'
                }),
            'golo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'numero': 'Número do Penálti',
            'golo': 'Golo?'
        }

class P_FaltaForm(forms.ModelForm):
    clube = forms.ModelChoiceField(
        queryset=P_Clube.objects.none(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'clube-select'
        }),
        empty_label="Escolha o clube"
    )
    jogador = forms.ModelChoiceField(
        queryset=P_Jogador.objects.none(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'jogador-select'
        }),
        empty_label="Escolha o jogador"
    )
    
    def __init__(self, *args, jogo=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['minuto'].initial = 0        
        self.fields['compensacao'].initial = 0
        
        if jogo:
            # Verifica se os clubes existem
            if jogo.clube_casa and jogo.clube_fora:
                self.fields['clube'].queryset = P_Clube.objects.filter(
                    _id__in=[jogo.clube_casa._id, jogo.clube_fora._id]
                )
            
            # Se estivermos editando uma falta existente
            if self.instance and self.instance.pk and self.instance.clube:
                equipa = None
                # Determina qual equipa baseado no clube
                if jogo.clube_casa and self.instance.clube._id == jogo.clube_casa._id:
                    equipa = jogo.equipa_casa
                elif jogo.clube_fora and self.instance.clube._id == jogo.clube_fora._id:
                    equipa = jogo.equipa_fora
                    
                if equipa:
                    self.fields['jogador'].queryset = P_Jogador.objects.filter(
                        equipa=equipa
                    )
                    
        ## IDs
        self.fields['clube'].label_from_instance = lambda obj: f"{obj.nome}"
        self.fields['clube'].to_python = convert_to_clube
        self.fields['jogador'].label_from_instance = lambda obj: f"{obj.nome}"
        self.fields['jogador'].to_python = convert_to_jogador
        
        self.jogo = jogo
        
    class Meta:
        model = P_Falta
        fields = ['clube', 'jogador', 'minuto', 'compensacao', 'cartao', 'cartao_cor']
        widgets = {
            'minuto': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Duração', 
                'min': 0,
                'required': 'required'
            }),
            'compensacao': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Compensação', 
                'min': 0,
                'required': 'required'
            }),
            'cartao': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'cartao_cor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cor do Cartão'}),
        }
        labels = {
            'minuto': 'Minuto da Falta',
            'compensacao': 'Compensação (Se existir)',
            'cartao': 'Recebeu Cartão?',
            'cartao_cor': 'Cor do Cartão'
        }
        
class P_SubstituicaoForm(forms.ModelForm):
    clube = forms.ModelChoiceField(
        queryset=P_Clube.objects.none(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'clube-select'
        }),
        empty_label="Escolha o clube"
    )
    jogador_sai = forms.ModelChoiceField(
        queryset=P_Jogador.objects.none(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'jogador-sai-select'
        }),
        empty_label="Escolha o jogador que saiu"
    )
    jogador_entra = forms.ModelChoiceField(
        queryset=P_Jogador.objects.none(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'jogador-entra-select'
        }),
        empty_label="Escolha o jogador que entrou"
    )
    
    def __init__(self, *args, jogo=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['minuto'].initial = 0        
        self.fields['compensacao'].initial = 0
        
        if jogo:
            # Verifica se os clubes existem
            if jogo.clube_casa and jogo.clube_fora:
                self.fields['clube'].queryset = P_Clube.objects.filter(
                    _id__in=[jogo.clube_casa._id, jogo.clube_fora._id]
                )
            
            # Se estivermos editando uma substituição existente
            if self.instance and self.instance.pk and self.instance.clube:
                equipa = None
                # Determina qual equipa baseado no clube
                if jogo.clube_casa and self.instance.clube._id == jogo.clube_casa._id:
                    equipa = jogo.equipa_casa
                elif jogo.clube_fora and self.instance.clube._id == jogo.clube_fora._id:
                    equipa = jogo.equipa_fora
                    
                if equipa:
                    jogadores_query = P_Jogador.objects.filter(equipa=equipa)
                    self.fields['jogador_sai'].queryset = jogadores_query
                    self.fields['jogador_entra'].queryset = jogadores_query
                    
        ## IDs
        self.fields['clube'].label_from_instance = lambda obj: f"{obj.nome}"
        self.fields['clube'].to_python = convert_to_clube
        self.fields['jogador_sai'].label_from_instance = lambda obj: f"{obj.nome}"
        self.fields['jogador_sai'].to_python = convert_to_jogador 
        self.fields['jogador_entra'].label_from_instance = lambda obj: f"{obj.nome}"
        self.fields['jogador_entra'].to_python = convert_to_jogador
        
        self.jogo = jogo
        
    def clean(self):
        cleaned_data = super().clean()
        jogador_sai = cleaned_data.get('jogador_sai')
        jogador_entra = cleaned_data.get('jogador_entra')
        
        if jogador_sai and jogador_entra and jogador_sai == jogador_entra:
            raise forms.ValidationError({
                'jogador_entra': 'O jogador que entra não pode ser o mesmo que sai.'
            })
            
        return cleaned_data
        
    class Meta:
        model = P_Substituicao
        fields = ['clube', 'jogador_sai', 'jogador_entra', 'minuto', 'compensacao']
        widgets = {
            'minuto': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Duração', 
                'min': 0,
                'required': 'required'
            }),
            'compensacao': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Compensação', 
                'min': 0,
                'required': 'required'
            }),
        }
        labels = {
            'minuto': 'Minuto da Substituição',
            'compensacao': 'Compensação (Se existir)',
        }