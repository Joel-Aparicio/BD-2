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

class Competicao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    ano = models.IntegerField()

    def __str__(self):
        return f"{self.nome} ({self.ano})"


class Jogo(models.Model):
    ano = models.IntegerField()
    dia = models.DateField()
    hora = models.TimeField()
    clube_casa = models.ForeignKey(Clube, on_delete=models.CASCADE, related_name='jogos_casa')
    clube_fora = models.ForeignKey(Clube, on_delete=models.CASCADE, related_name='jogos_fora')
    competicao = models.ForeignKey(Competicao, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.clube_casa} vs {self.clube_fora} - {self.competicao.nome} ({self.dia})"