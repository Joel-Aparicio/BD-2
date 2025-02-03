from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import P_Equipa, P_Jogador, P_Clube

#ESTE FICHEIRO TEM O OBJETIVO DE APAGAR CORRETAMENTE AS REFERENCIAS DE OUTRAS TABELAS/OBJETOS




#--- APAGAR EQUIPA ---
@receiver(post_delete, sender=P_Equipa)
def limpar_referencias_EquipaJogador(sender, instance, **kwargs):
    if instance._id is not None:
        P_Jogador.objects.filter(equipa=instance._id).update(equipa=None) #Atualiza o objectID da equipa para nulo





#--- APAGAR CLUBE ---
@receiver(post_delete, sender=P_Clube)
def limpar_referencias_Clube(sender, instance, **kwargs):
    # Apagar todas as equipas relacionadas ao clube
    P_Equipa.objects.filter(clube=instance).delete()
    
    # Atualizar o campo 'clube' nos jogadores para null
    P_Jogador.objects.filter(clube=instance).update(clube=None) #Atualiza o objectID do clube para nulo




