from django.db import models
from django.utils import timezone
from djongo import models
from bson import ObjectId

class Utilizador(models.Model):
    utilizador_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, unique=True)
    palavra_passe = models.CharField(max_length=200)
    ser_admin = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)  # Coluna para armazenar o último login
    is_active = models.BooleanField(default=True)  # Substitui o campo 'ativo'

    class Meta:
        db_table = 'p_utilizador'  # Nome exato da tabela no banco de dados

    def __str__(self):
        return self.nome

# MONGODB 
class P_Associacao(models.Model): #FEITO
    _id = models.ObjectIdField(primary_key=True, default=ObjectId) #RECEBE ID DO MONGODB
    nome = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True, default='')
    pais = models.CharField(max_length=100)
    imagem = models.URLField(blank=True, null=True, default='')

    class Meta:
        db_table = "p_associacoes"
        app_label = 'BD2_Trabalhofinal.App'
    
    def __str__(self):
        return self.nome
     
    #ID DO MONGODB
    def get_id(self):
        return str(self._id)

class P_Estadio(models.Model): #FEITO
    _id = models.ObjectIdField(primary_key=True, default=ObjectId) #RECEBE ID DO MONGODB
    nome = models.CharField(max_length=255)
    pais = models.CharField(max_length=100)
    cidade = models.CharField(max_length=255)
    inauguracao = models.IntegerField(blank=True)

    class Meta:
        db_table = "p_estadios"
        app_label = 'BD2_Trabalhofinal.App'
        
    def __str__(self):
        return self.nome
     
    #ID DO MONGODB
    def get_id(self):
        return str(self._id)

class P_Posicao(models.Model): #FEITO
    _id = models.ObjectIdField(primary_key=True, default=ObjectId) #RECEBE ID DO MONGODB
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    
    class Meta:
        db_table = "p_posicoes"
        app_label = 'BD2_Trabalhofinal.App'
        
    def __str__(self):
        return self.nome
     
    #ID DO MONGODB
    def get_id(self):
        return str(self._id)
        
class P_Jogador(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId) #RECEBE ID DO MONGODB
    nome = models.CharField(max_length=255)
    idade = models.IntegerField(blank=True, null=True)
    imagem = models.URLField(blank=True, null=True, default='')
    altura = models.IntegerField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    nacionalidade = models.CharField(max_length=100, blank=True, null=True)
    num_camisola = models.IntegerField()
    valor_de_mercado = models.FloatField(blank=True, null=True)
    num_jogos = models.IntegerField(blank=True, null=True)
    num_golos = models.IntegerField(blank=True, null=True)
    situacao = models.CharField(max_length=50)
    #posicao = models.CharField(max_length=24, blank=True, null=True)  # String para armazenar o ObjectId como texto
    #posicao = models.ObjectIdField(blank=True, null=True)  # Apenas o ID da posição
    #posicao = models.JSONField(blank=True, null=True)
    #historico = models.ArrayField(
     #   model_container=models.JSONField(),
      #  blank=True, null=True
    #)

    class Meta:
        db_table = "p_jogadores"
        app_label = 'BD2_Trabalhofinal.App'
        
     #ID DO MONGODB
    def get_id(self):
        return str(self._id)

class P_Clube(models.Model):
    nome = models.CharField(max_length=255)
    ano_fundacao = models.DateField(blank=True, null=True)
    pais = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    extinto = models.BooleanField()
    associacao = models.JSONField(blank=True, null=True)  # Contém associacao_id e nome
    estadio = models.JSONField(blank=True, null=True)     # Contém estadio_id e nome

    class Meta:
        db_table = "p_clubes"
        app_label = 'BD2_Trabalhofinal.App'

    def __str__(self):
        return self.nome

class P_FormatoCompeticao(models.Model): # FEITO
    _id = models.ObjectIdField(primary_key=True, default=ObjectId) #RECEBE ID DO MONGODB
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)

    class Meta:
        db_table = "p_formatos_competicao"
        app_label = 'BD2_Trabalhofinal.App'
        
    def __str__(self):
        return self.nome
     
    #ID DO MONGODB
    def get_id(self):
        return str(self._id)

class P_Competicao(models.Model):
    nome = models.CharField(max_length=255)
    ano = models.IntegerField()
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
    formato = models.JSONField(blank=True, null=True)
    vencedor = models.JSONField(blank=True, null=True)

    class Meta:
        db_table = "p_competicoes"
        app_label = 'BD2_Trabalhofinal.App'

class P_Jogo(models.Model):
    duracao = models.CharField(max_length=50, blank=True, null=True)
    prolongamento = models.BooleanField(blank=True, null=True)
    penaltis = models.BooleanField(blank=True, null=True)
    dia = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=50)
    estadio = models.JSONField(blank=True, null=True)
    equipa_casa = models.JSONField(blank=True, null=True)
    equipa_fora = models.JSONField(blank=True, null=True)
    #golos = models.ArrayField(
     #   model_container=models.JSONField(),
      #  blank=True, null=True
    #)
    #faltas = models.ArrayField(
     #   model_container=models.JSONField(),
      #  blank=True, null=True
    #)
    #substituicoes = models.ArrayField(
     #   model_container=models.JSONField(),
      #  blank=True, null=True
    #)

    class Meta:
        db_table = "p_jogos"
        app_label = 'BD2_Trabalhofinal.App'

class P_Equipa(models.Model):
    clube = models.ForeignKey(P_Clube, on_delete=models.CASCADE, related_name="equipas")
    nome = models.CharField(max_length=255)
    ativa = models.BooleanField()
    jogadores = models.JSONField(blank=True, null=True)  # Array contendo objetos de jogadores

    class Meta:
        db_table = "p_equipas"
        app_label = 'BD2_Trabalhofinal.App'

    def __str__(self):
        return self.nome
        
class P_EquipaFavorita(models.Model):
    utilizador_id = models.IntegerField()
    equipa = models.ForeignKey(P_Equipa, on_delete=models.CASCADE, related_name="favoritos")

    class Meta:
        db_table = "p_equipas_favoritas"
        app_label = 'BD2_Trabalhofinal.App'

    def __str__(self):
        return f"Favorita do Utilizador {self.utilizador_id}: {self.equipa.nome}"


# --- TEMP ---
class AssociacaoFutebol(models.Model):
    nome = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Clube(models.Model):
    nome = models.CharField(max_length=100)
    estadio = models.CharField(max_length=100)
    ano_fundacao = models.IntegerField()
    alcunha = models.CharField(max_length=50, null=True, blank=True) # Permite valores nulos
    pais = models.CharField(max_length=100, null=True, blank=True) # Permite valores nulos
    cidade = models.CharField(max_length=100, null=True, blank=True)  # Permite valores nulos

    def __str__(self):
        return f"{self.nome} ({self.ano_fundacao})"

class FormatoCompeticao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
        
class Competicao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    ano = models.IntegerField()
    formato_competicao = models.ForeignKey(
        FormatoCompeticao, 
        on_delete=models.CASCADE, 
        related_name="competicoes",
        null=False,
    )  # Relação com FormatoCompeticao

    def __str__(self):
        return f"{self.nome} ({self.ano})"



class Jogo(models.Model):
    ano = models.IntegerField()
    dia = models.DateField()
    hora = models.TimeField()
    terminado = models.BooleanField(default=False)  #Campo bool com valor padrão False
    clube_casa = models.ForeignKey(Clube, on_delete=models.CASCADE, related_name='jogos_casa')
    clube_fora = models.ForeignKey(Clube, on_delete=models.CASCADE, related_name='jogos_fora')
    competicao = models.ForeignKey(Competicao, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.clube_casa} vs {self.clube_fora} - {self.competicao.nome} ({self.dia})"
     
     
class PosicaoJogador(models.Model):
    nome = models.CharField(max_length=25)
    descricao = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        if self.descricao is None or self.descricao.strip() == "":
            return self.nome
        else:
            return f"{self.nome} ({self.descricao})"

            
            
class Jogador(models.Model):
    nome = models.CharField(max_length=100)  #Nome do jogador
    nacionalidade = models.CharField(max_length=100)  #Nacionalidade do jogador
    situacao = models.CharField(max_length=50)  #Situação do jogador (e.g., ativo, lesionado, aposentado)
    idade = models.IntegerField()  #Idade do jogador
    num_camisola = models.IntegerField()  #Número da camisola do jogador
    posicao = models.ForeignKey(
        PosicaoJogador, 
        on_delete=models.CASCADE, 
        related_name="jogadores"
    )  # Relação com PosicaoJogador

    def __str__(self):
        return f"{self.num_camisola}. {self.nome}"
        
class Equipa(models.Model):
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)  # Campo booleano com valor padrão True
    clube = models.ForeignKey(
        Clube, 
        on_delete=models.CASCADE, 
        related_name='equipas'
    )  #Relacionado a um Clube

    def __str__(self):
        return self.nome