from django.db import models
from django.utils import timezone
from djongo import models
from bson import ObjectId
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UtilizadorManager(BaseUserManager):
    def create_user(self, email, nome, palavra_passe=None, **extra_fields):
        if not email:
            raise ValueError('O utilizador deve ter um email.')
        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, **extra_fields)
        user.set_password(palavra_passe)  # Usa hashing para a palavra-passe
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, palavra_passe=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, nome, palavra_passe, **extra_fields)

class Utilizador(AbstractBaseUser, PermissionsMixin):
    utilizador_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)  # Substitui 'ativo'
    is_staff = models.BooleanField(default=False)  # Necessário para admins
    

    objects = UtilizadorManager()

    USERNAME_FIELD = 'email'  # Campo único usado para login
    REQUIRED_FIELDS = ['nome']  # Campos obrigatórios além do `USERNAME_FIELD`

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
    imagem = models.URLField(blank=True, null=True, default='')
    pais = models.CharField(max_length=100)
    cidade = models.CharField(max_length=255)
    inauguracao = models.IntegerField(blank=True)
    estado = models.CharField(max_length=10)
    lotacao = models.IntegerField(blank=True)

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
    descricao = models.TextField(blank=True, null=True, default='') #Opcional
    
    class Meta:
        db_table = "p_posicoes"
        app_label = 'BD2_Trabalhofinal.App'
        
    def __str__(self):
        return self.nome
     
    #ID DO MONGODB
    def get_id(self):
        return str(self._id)

class P_Clube(models.Model): #FEITO
    _id = models.ObjectIdField(primary_key=True, default=ObjectId) #RECEBE ID DO MONGODB
    nome = models.CharField(max_length=255)
    imagem = models.URLField(blank=True, null=True, default='')
    ano_fundacao = models.IntegerField(blank=True, null=True)
    ano_extinto = models.IntegerField(blank=True, null=True)
    alcunhas = models.CharField(max_length=100, blank=True)
    pais = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=10)
    associacao = models.ForeignKey(P_Associacao, on_delete=models.SET_NULL, null=True, related_name="clubes")
    estadio = models.ForeignKey(P_Estadio, on_delete=models.SET_NULL, null=True, related_name="clubes")

    class Meta:
        db_table = "p_clubes"
        app_label = 'BD2_Trabalhofinal.App'

    def __str__(self):
        return self.nome
    #ID DO MONGODB
    def get_id(self):
        return str(self._id)
        
class P_Equipa(models.Model): #FEITO
    _id = models.ObjectIdField(primary_key=True, default=ObjectId) #RECEBE ID DO MONGODB
    clube = models.ForeignKey(P_Clube, on_delete=models.CASCADE, related_name="equipas")
    nome = models.CharField(max_length=255)
    estado = models.CharField(max_length=10)

    class Meta:
        db_table = "p_equipas"
        app_label = 'BD2_Trabalhofinal.App'

    def __str__(self):
        return self.nome
    
    #ID DO MONGODB
    def get_id(self):
        return str(self._id)
    
class P_FormatoCompeticao(models.Model): # FEITO
    _id = models.ObjectIdField(primary_key=True, default=ObjectId) #RECEBE ID DO MONGODB
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    valor_de_mercado = models.FloatField(blank=True)

    class Meta:
        db_table = "p_formatos_competicao"
        app_label = 'BD2_Trabalhofinal.App'
        
    def __str__(self):
        return self.nome
     
    #ID DO MONGODB
    def get_id(self):
        return str(self._id)

class P_Competicao(models.Model): # FEITO
    _id = models.ObjectIdField(primary_key=True, default=ObjectId) #RECEBE ID DO MONGODB
    nome = models.CharField(max_length=255)
    imagem = models.URLField(blank=True, null=True, default='')
    data_inicio = models.DateField(blank=True, null=True)
    data_fim = models.DateField(blank=True, null=True)
    finalizado = models.BooleanField()
    formato = models.ForeignKey(P_FormatoCompeticao, on_delete=models.CASCADE, related_name="competicoes")
    vencedor = models.ForeignKey(P_Clube, on_delete=models.CASCADE, related_name="competicoes")

    class Meta:
        db_table = "p_competicoes"
        app_label = 'BD2_Trabalhofinal.App'
    #ID DO MONGODB
    def get_id(self):
        return str(self._id)


class P_Jogo(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)
    dia = models.DateField(blank=True, null=True)
    hora = models.CharField(max_length=6) # hh:mm +1 extra
    estado = models.CharField(max_length=50)
    duracao = models.IntegerField(blank=True, null=True)
    prolongamento = models.BooleanField(default=False)
    penaltis = models.BooleanField(default=False)
    
    #Chaves Estrangeiras
    competicao = models.ForeignKey(P_Competicao, on_delete=models.CASCADE, related_name="jogos")
    estadio = models.ForeignKey(P_Estadio, on_delete=models.CASCADE, related_name="jogos")
    clube_casa = models.ForeignKey(P_Clube, on_delete=models.CASCADE, related_name="jogos")
    clube_fora = models.ForeignKey(P_Clube, on_delete=models.CASCADE, related_name="jogos")
    equipa_casa = models.ForeignKey(P_Equipa, on_delete=models.CASCADE, related_name="jogos")
    equipa_fora = models.ForeignKey(P_Equipa, on_delete=models.CASCADE, related_name="jogos")
    vencedor = models.ForeignKey(P_Clube, on_delete=models.CASCADE, related_name="jogos")
    
    class Meta:
        db_table = "p_jogos"
        app_label = 'BD2_Trabalhofinal.App'
        
    def get_id(self):
        return str(self._id)

class P_Jogador(models.Model): #FEITO
    _id = models.ObjectIdField(primary_key=True, default=ObjectId) #RECEBE ID DO MONGODB
    clube = models.ForeignKey(P_Clube, on_delete=models.SET_NULL, null=True, related_name="jogadores")
    posicao = models.ForeignKey(P_Posicao, on_delete=models.SET_NULL, null=True, related_name="jogadores")
    equipa = models.ForeignKey(P_Equipa, on_delete=models.SET_NULL, null=True, blank=True, related_name='jogadores')
    nome = models.CharField(max_length=255)
    idade = models.IntegerField(blank=True)
    imagem = models.URLField(blank=True, null=True, default='')
    altura = models.IntegerField(blank=True)
    peso = models.FloatField(blank=True)
    nacionalidade = models.CharField(max_length=100, blank=True)
    num_camisola = models.IntegerField()
    valor_de_mercado = models.FloatField(blank=True)
    situacao = models.CharField(max_length=50)

    class Meta:
        db_table = "p_jogadores"
        app_label = 'BD2_Trabalhofinal.App'
        
    def __str__(self):
        return self.nome
        
    #ID DO MONGODB
    def get_id(self):
        return str(self._id)
        
class P_ClubeFavorito(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId) #RECEBE ID DO MONGODB => Só para o caso de ser preciso
    utilizador_id = models.IntegerField()
    clube = models.ForeignKey(P_Clube, on_delete=models.CASCADE, related_name="favoritos")

    class Meta:
        db_table = "p_clubes_favoritos"
        app_label = 'BD2_Trabalhofinal.App'

    def __str__(self):
        return f"Favorita do Utilizador {self.utilizador_id}: {self.equipa.nome}"
    
    #ID DO MONGODB
    def get_id(self):
        return str(self._id)
        
# --- ESTATÍSTICAS JOGOS
class P_Golo(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId) #RECEBE ID DO MONGODB
    jogo = models.ForeignKey(P_Jogo, on_delete=models.CASCADE, related_name="golos")
    jogador = models.ForeignKey(P_Jogador, on_delete=models.SET_NULL, null=True, blank=True, related_name="golos")
    clube = models.ForeignKey(P_Clube, on_delete=models.SET_NULL, null=True, blank=True, related_name="golos")
    penalti = models.BooleanField(default=False)
    minuto = models.IntegerField(blank=True)
    compensacao = models.IntegerField(blank=True)

    class Meta:
        db_table = "p_golos"
        app_label = 'BD2_Trabalhofinal.App'
        
    def __str__(self):
        return f"Golo {self.jogador.nome} -  {self.clube.nome}"
        
    #ID DO MONGODB
    def get_id(self):
        return str(self._id)
        
class P_Penalti(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId) #RECEBE ID DO MONGODB
    jogo = models.ForeignKey(P_Jogo, on_delete=models.CASCADE, related_name="golos")
    jogador = models.ForeignKey(P_Jogador, on_delete=models.SET_NULL, null=True, blank=True, related_name="golos")
    clube = models.ForeignKey(P_Clube, on_delete=models.SET_NULL, null=True, blank=True, related_name="golos")
    numero = models.IntegerField(blank=False)
    golo = models.BooleanField(default=False)

    class Meta:
        db_table = "p_penaltis"
        app_label = 'BD2_Trabalhofinal.App'
        
    def __str__(self):
        return f"Penalti {self.jogador.nome} -  {self.clube.nome}"
        
    #ID DO MONGODB
    def get_id(self):
        return str(self._id)
        
class P_Falta(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId) #RECEBE ID DO MONGODB
    jogo = models.ForeignKey(P_Jogo, on_delete=models.CASCADE, related_name="golos")
    jogador = models.ForeignKey(P_Jogador, on_delete=models.SET_NULL, null=True, blank=True, related_name="golos")
    clube = models.ForeignKey(P_Clube, on_delete=models.SET_NULL, null=True, blank=True, related_name="golos")
    cartao = models.BooleanField(default=False)
    cartao_cor = models.CharField(max_length=10) # Vermelho ou Amarelo
    minuto = models.IntegerField(blank=True)
    compensacao = models.IntegerField(blank=True)

    class Meta:
        db_table = "p_faltas"
        app_label = 'BD2_Trabalhofinal.App'
        
    def __str__(self):
        return f"Faltas {self.jogador.nome} -  {self.clube.nome}"
        
    #ID DO MONGODB
    def get_id(self):
        return str(self._id)
        
class P_Substituicao(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId) #RECEBE ID DO MONGODB
    jogo = models.ForeignKey(P_Jogo, on_delete=models.CASCADE, related_name="golos")
    jogador_entra = models.ForeignKey(P_Jogador, on_delete=models.SET_NULL, null=True, blank=True, related_name="golos")
    jogador_sai = models.ForeignKey(P_Jogador, on_delete=models.SET_NULL, null=True, blank=True, related_name="golos")
    clube = models.ForeignKey(P_Clube, on_delete=models.SET_NULL, null=True, blank=True, related_name="golos")
    minuto = models.IntegerField(blank=True)
    compensacao = models.IntegerField(blank=True)

    class Meta:
        db_table = "p_substituicoes"
        app_label = 'BD2_Trabalhofinal.App'
        
    def __str__(self):
        return f"Sai {self.jogador_sai.nome} - Entra {self.jogador_entra.nome}"
        
    #ID DO MONGODB
    def get_id(self):
        return str(self._id)
        
        
        