# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




 
class AppAssociacaofutebol(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    url = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'App_associacaofutebol'



class AppClube(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    alcunha = models.CharField(max_length=50, blank=True, null=True)
    estadio = models.CharField(max_length=100)
    ano_fundacao = models.IntegerField()
    cidade = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'App_clube'



class AppCompeticao(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    ano = models.IntegerField()
    formato_competicao = models.ForeignKey('AppFormatocompeticao', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'App_competicao'



class AppEquipa(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    ativo = models.BooleanField()
    clube = models.ForeignKey(AppClube, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'App_equipa'



class AppFormatocompeticao(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    class Meta:
        managed = False
        db_table = 'App_formatocompeticao'



class AppJogador(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)
    situacao = models.CharField(max_length=50)
    idade = models.IntegerField()
    num_camisola = models.IntegerField()
    posicao = models.ForeignKey('AppPosicaojogador', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'App_jogador'





class AppJogo(models.Model):
    id = models.BigAutoField(primary_key=True)
    ano = models.IntegerField()
    dia = models.DateField()
    hora = models.TimeField()
    clube_casa = models.ForeignKey(AppClube, models.DO_NOTHING)
    clube_fora = models.ForeignKey(AppClube, models.DO_NOTHING)
    competicao = models.ForeignKey(AppCompeticao, models.DO_NOTHING)
    terminado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'App_jogo'




class AppPosicaojogador(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=25)
    descricao = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'App_posicaojogador'




class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'




class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)





class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)





class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'





class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)






class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)




class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'




class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)






class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'








class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'




class Utilizador(models.Model):
    utilizador_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=200)
    palavra_passe = models.CharField(max_length=200)
    seradmin = models.BooleanField()
    ativo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'utilizador'






















