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
    imagem = models.URLField(blank=True, null=True, default='')
    pais = models.CharField(max_length=100)
    cidade = models.CharField(max_length=255)
    inauguracao = models.IntegerField(blank=True)
    ativo = models.BooleanField()
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
    extinto = models.BooleanField()
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
    ativa = models.BooleanField()

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
    
    class Meta:
        db_table = "p_jogos"
        app_label = 'BD2_Trabalhofinal.App'
        
    def save(self, *args, **kwargs):
        try:
            print("=== SAVE DEBUG ===")
            print("Saving jogo:", self.__dict__)
            
            # Validar campos obrigatórios antes de salvar
            required_fields = {
                'dia': self.dia,
                'estado': self.estado,
                'competicao': self.competicao,
                'estadio': self.estadio,
                'clube_casa': self.clube_casa,
                'clube_fora': self.clube_fora,
                'equipa_casa': self.equipa_casa,
                'equipa_fora': self.equipa_fora
            }
            
            for field_name, value in required_fields.items():
                if value is None:
                    raise ValidationError(f'O campo {field_name} é obrigatório')
            
            super().save(*args, **kwargs)
            print("Save successful")
        except Exception as e:
            print("Error in save method:", str(e))
            raise
        
    def get_id(self):
        return str(self._id)

class P_Jogador(models.Model): #FEITO +- => Falta Historico 
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
    num_jogos = models.IntegerField(blank=True, null=True)
    num_golos = models.IntegerField(blank=True, null=True)
    situacao = models.CharField(max_length=50)
    #historico = models.ArrayField(
     #   model_container=models.JSONField(),
      #  blank=True, null=True
    #)

    class Meta:
        db_table = "p_jogadores"
        app_label = 'BD2_Trabalhofinal.App'
        
    def __str__(self):
        return self.nome
        
    #ID DO MONGODB
    def get_id(self):
        return str(self._id)
        
class P_EquipaFavorita(models.Model):
    utilizador_id = models.IntegerField()
    equipa = models.ForeignKey(P_Equipa, on_delete=models.CASCADE, related_name="favoritos")

    class Meta:
        db_table = "p_equipas_favoritas"
        app_label = 'BD2_Trabalhofinal.App'

    def __str__(self):
        return f"Favorita do Utilizador {self.utilizador_id}: {self.equipa.nome}"
