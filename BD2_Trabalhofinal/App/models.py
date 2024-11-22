from django.db import models


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
