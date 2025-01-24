from django import forms
from django.core.exceptions import ValidationError
from bson import ObjectId  # Adicione esta importação!
from .models import P_Posicao, P_Associacao, P_FormatoCompeticao, P_Estadio, P_Jogador, P_Clube, P_Equipa, P_Competicao, P_Jogo


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
    class Meta:
        model = P_Estadio
        fields = ['nome', 'imagem', 'pais', 'cidade', 'inauguracao', 'lotacao', 'ativo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o nome do Estádio'}),
            'imagem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o url da imagem'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o país'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva a cidade'}),
            'inauguracao': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ano de Inauguração', 'min': 0}),
            'lotacao': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Lotacao', 'min': 0}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'})  #checkbox
        }
        labels = {
            'nome': 'Nome do Estádio',
            'imagem': 'Imagem do Estádio',
            'pais': 'País',
            'cidade': 'Cidade',
            'inauguracao': 'Ano de Inauguração',
            'lotacao': 'Lotação do Estádio',
            'ativo': 'Ativo'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['inauguracao'].initial = 1900  # Define o valor padrão para o formulário
        self.fields['ativo'].initial = True  # Define o valor padrão para o formulário
        
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

   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       # Configurações existentes
       self.fields['peso'].initial = 60.0
       self.fields['num_camisola'].initial = 0
       self.fields['valor_de_mercado'].initial = 0.0
       self.fields['num_jogos'].initial = 0
       self.fields['num_golos'].initial = 0
       self.fields['situacao'].initial = 'Ativo'
       self.fields['altura'].initial = 0
       self.fields['idade'].initial = 0
       
       # Configurar label_from_instance para clube, posição e equipa
       self.fields['clube'].label_from_instance = lambda obj: f"{obj.nome}"
       self.fields['equipa'].label_from_instance = lambda obj: f"{obj.nome}"
       self.fields['posicao'].label_from_instance = lambda obj: f"{obj.nome} ({obj.descricao})" if obj.descricao else f"{obj.nome}"
       
       # Configurar to_python para clube, posição e equipa
       self.fields['clube'].to_python = self.convert_to_clube
       self.fields['equipa'].to_python = self.convert_to_equipa
       self.fields['posicao'].to_python = self.convert_to_posicao

       # Se estiver editando um jogador existente
       if 'instance' in kwargs and kwargs['instance']:
           jogador = kwargs['instance']
           if jogador.clube:
               # Filtra as equipas do clube selecionado
               self.fields['equipa'].queryset = P_Equipa.objects.filter(clube=jogador.clube)

   def convert_to_clube(self, value):
       if not value:
           return None
       try:
           if isinstance(value, str):
               return P_Clube.objects.get(_id=ObjectId(value))
           return value
       except Exception as e:
           raise ValidationError('Clube inválido')

   def convert_to_equipa(self, value):
       if not value:
           return None
       try:
           if isinstance(value, str):
               return P_Equipa.objects.get(_id=ObjectId(value))
           return value
       except Exception as e:
           raise ValidationError('Equipa inválida')

   def convert_to_posicao(self, value):
       if not value:
           return None
       try:
           if isinstance(value, str):
               return P_Posicao.objects.get(_id=ObjectId(value))
           return value
       except Exception as e:
           raise ValidationError('Posição inválida')

   def clean(self):
       cleaned_data = super().clean()
       # Converte Strings vazias em None para campos URL
       if 'imagem' in cleaned_data and cleaned_data['imagem'] == '':
           cleaned_data['imagem'] = None
       return cleaned_data

   class Meta:
       model = P_Jogador
       fields = ['nome', 'idade', 'imagem', 'altura', 'peso', 'nacionalidade', 
                'num_camisola', 'valor_de_mercado', 'num_jogos', 'num_golos', 
                'situacao', 'posicao', 'clube', 'equipa']
       widgets = {
           'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o nome do Jogador'}),
           'idade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Idade', 'min': 0}),
           'imagem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o url da imagem'}),
           'altura': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Altura em centímetros', 'min': 0}),
           'peso': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Peso do Jogador', 'min': 0}),
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ano_fundacao'].initial = 1900
        self.fields['ano_extinto'].initial = 0
        self.fields['extinto'].initial = False
        self.fields['associacao'].label_from_instance = lambda obj: f"{obj.nome} ({obj.pais})"
        # Adicionar o conversor para a associação e estadio
        self.fields['associacao'].to_python = self.convert_to_associacao
        self.fields['estadio'].to_python = self.convert_to_estadio

    def convert_to_associacao(self, value):
        if not value:
            return None
        try:
            print("=== CONVERT ASSOCIACAO DEBUG ===")
            print("Received value:", value)
            print("Type of value:", type(value))
            if isinstance(value, str):
                object_id = ObjectId(value)
                print("Created ObjectId:", object_id)
                associacao = P_Associacao.objects.get(_id=object_id)
                print("Found associacao:", associacao)
                return associacao
            return value
        except Exception as e:
            print("Error in convert_to_associacao:", str(e))
            raise ValidationError('Associação inválida')
    
    def convert_to_estadio(self, value):
        if not value:
            return None
        try:
            print("=== CONVERT ESTADIO DEBUG ===")
            print("Received value:", value)
            print("Type of value:", type(value))
            if isinstance(value, str):
                object_id = ObjectId(value)
                print("Created ObjectId:", object_id)
                estadio = P_Estadio.objects.get(_id=object_id)
                print("Found estadio:", estadio)
                return estadio
            return value
        except Exception as e:
            print("Error in convert_to_estadio:", str(e))
            raise ValidationError('estadio inválida')

    class Meta:
        model = P_Clube
        fields = ['nome', 'imagem', 'ano_fundacao', 'ano_extinto', 'alcunhas', 'pais', 'cidade', 'extinto', 'associacao', 'estadio']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o nome do Clube'}),
            'imagem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o url da imagem'}),
            'ano_fundacao': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Fundação', 'min': 0}),
            'ano_extinto': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Extinto', 'min': 0}),
            'alcunhas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira as alcunhas'}),
            'pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva o país'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva a cidade'}),         
            'extinto': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
        labels = {
            'nome': 'Nome do Clube',
            'imagem': 'Imagem do Clube',
            'ano_fundacao': 'Ano Fundado',
            'ano_extinto': 'Ano Extinto (Caso esteja)',
            'alcunhas': 'Alcunhas',
            'pais': 'País',
            'cidade': 'Cidade',
            'extinto': 'Extinto?',
            'associacao': 'Associação',
            'estadio': 'Estádio (Se existir)'
        }
    
    def clean(self):
        cleaned_data = super().clean()
        if 'imagem' in cleaned_data and cleaned_data['imagem'] == '':
            cleaned_data['imagem'] = None
        return cleaned_data
        
        
class P_EquipaForm(forms.ModelForm):
    clube = forms.ModelChoiceField(
        queryset=P_Clube.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Escolha o clube"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['clube'].label_from_instance = lambda obj: f"{obj.nome}"
        self.fields['clube'].to_python = self.convert_to_clube
        self.fields['ativa'].initial = True #Coloca a equipa ativa como Default
        

    def convert_to_clube(self, value):
        if not value:
            return None
        try:
            print("=== CONVERT DEBUG ===")
            print("Received value:", value)
            print("Type of value:", type(value))
            if isinstance(value, str):
                object_id = ObjectId(value)
                print("Created ObjectId:", object_id)
                clube = P_Clube.objects.get(_id=object_id)
                print("Found clube:", clube)
                return clube
            return value
        except Exception as e:
            print("Error in convert_to_clube:", str(e))
            raise ValidationError('Clube inválido')

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
        

class P_CompeticaoForm(forms.ModelForm):
    formato = forms.ModelChoiceField(
        queryset=P_FormatoCompeticao.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Escolha o Formato"
    )

    vencedor = forms.ModelChoiceField(
        queryset=P_Clube.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Escolha o Clube Vencedor",
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
        self.fields['formato'].to_python = self.convert_to_formato
        self.fields['vencedor'].label_from_instance = lambda obj: f"{obj.nome}"
        self.fields['vencedor'].to_python = self.convert_to_clube

    def convert_to_formato(self, value):
        if not value:
            return None
        try:
            if isinstance(value, str):
                object_id = ObjectId(value)
                formato = P_FormatoCompeticao.objects.get(_id=object_id)
                return formato
            return value
        except Exception as e:
            raise ValidationError('Formato inválido')

    def convert_to_clube(self, value):
        if not value:
            return None
        try:
            if isinstance(value, str):
                object_id = ObjectId(value)
                clube = P_Clube.objects.get(_id=object_id)
                return clube
            return value
        except Exception as e:
            raise ValidationError('Clube inválido')

    def clean(self):
        cleaned_data = super().clean()
        # Converte Strings vazias em None para campos URL
        if 'imagem' in cleaned_data and cleaned_data['imagem'] == '':
            cleaned_data['imagem'] = None

        # Verifica se a competição está finalizada
        finalizado = cleaned_data.get('finalizado')
        vencedor = cleaned_data.get('vencedor')

        if finalizado and not vencedor:
            raise ValidationError('É necessário selecionar um clube vencedor quando a competição está finalizada.')

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
    
    # CASA
    clube_casa = forms.ModelChoiceField(
        queryset=P_Clube.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Escolha o Clube Casa"
    )
    equipa_casa = forms.ModelChoiceField(
        queryset=P_Equipa.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Escolha a Equipa Casa"
    )
    # FORA
    clube_fora = forms.ModelChoiceField(
        queryset=P_Clube.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Escolha o Clube Fora"
    )
    equipa_fora = forms.ModelChoiceField(
        queryset=P_Equipa.objects.all(),
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
        queryset=P_Estadio.objects.all(),
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
            
        # Converter hora para string no formato HH:mm
        hora = cleaned_data.get('hora')
        if hora:
            cleaned_data['hora'] = hora.strftime('%H:%M')
        
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['duracao'].initial = 90
        
        # CASA
        self.fields['clube_casa'].label_from_instance = lambda obj: f"{obj.nome}"
        self.fields['clube_casa'].to_python = self.convert_to_clube
        self.fields['equipa_casa'].label_from_instance = lambda obj: f"{obj.nome} ({obj.clube.nome})"
        self.fields['equipa_casa'].to_python = self.convert_to_equipa
        # FORA
        self.fields['clube_fora'].label_from_instance = lambda obj: f"{obj.nome}"
        self.fields['clube_fora'].to_python = self.convert_to_clube
        self.fields['equipa_fora'].label_from_instance = lambda obj: f"{obj.nome} ({obj.clube.nome})"
        self.fields['equipa_fora'].to_python = self.convert_to_equipa
        # COMPETICAO
        self.fields['competicao'].label_from_instance = lambda obj: f"{obj.nome}"
        self.fields['competicao'].to_python = self.convert_to_competicao
        # ESTADIO
        self.fields['estadio'].label_from_instance = lambda obj: f"{obj.nome}"
        self.fields['estadio'].to_python = self.convert_to_estadio
        
    # FUNÇÕES
    def convert_to_clube(self, value):
        if not value:
            return None
        try:
            if isinstance(value, str):
                object_id = ObjectId(value)
                clube = P_Clube.objects.get(_id=object_id)
                return clube
            return value
        except Exception as e:
            raise ValidationError('Clube inválido')
    
    def convert_to_equipa(self, value):
        if not value:
            return None
        try:
            if isinstance(value, str):
                object_id = ObjectId(value)
                equipa = P_Equipa.objects.get(_id=object_id)
                return equipa
            return value
        except Exception as e:
            raise ValidationError('Equipa inválida')
            
    def convert_to_competicao(self, value):
        if not value:
            return None
        try:
            if isinstance(value, str):
                object_id = ObjectId(value)
                competicao = P_Competicao.objects.get(_id=object_id)
                return competicao
            return value
        except Exception as e:
            raise ValidationError('Competição inválida')
            
    def convert_to_estadio(self, value):
        if not value:
            return None
        try:
            if isinstance(value, str):
                object_id = ObjectId(value)
                estadio = P_Estadio.objects.get(_id=object_id)
                return estadio
            return value
        except Exception as e:
            raise ValidationError('Estádio inválida')

    class Meta:
        model = P_Jogo
        fields = ['dia', 'hora', 'competicao', 'estadio', 'clube_casa', 'equipa_casa', 'clube_fora', 'equipa_fora', 'estado', 'duracao', 'prolongamento', 'penaltis']
        widgets = {
            'estado': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Estado do Jogo',
                'required': 'required'
            }),
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
