# Generated by Django 3.2 on 2025-01-20 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssociacaoFutebol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Clube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('estadio', models.CharField(max_length=100)),
                ('ano_fundacao', models.IntegerField()),
                ('alcunha', models.CharField(blank=True, max_length=50, null=True)),
                ('pais', models.CharField(blank=True, max_length=100, null=True)),
                ('cidade', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Competicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('ano', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FormatoCompeticao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PosicaoJogador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('descricao', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Utilizador',
            fields=[
                ('utilizador_id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('palavra_passe', models.CharField(max_length=200)),
                ('ser_admin', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'p_utilizador',
            },
        ),
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField()),
                ('dia', models.DateField()),
                ('hora', models.TimeField()),
                ('terminado', models.BooleanField(default=False)),
                ('clube_casa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jogos_casa', to='App.clube')),
                ('clube_fora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jogos_fora', to='App.clube')),
                ('competicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.competicao')),
            ],
        ),
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('nacionalidade', models.CharField(max_length=100)),
                ('situacao', models.CharField(max_length=50)),
                ('idade', models.IntegerField()),
                ('num_camisola', models.IntegerField()),
                ('posicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jogadores', to='App.posicaojogador')),
            ],
        ),
        migrations.CreateModel(
            name='Equipa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ativo', models.BooleanField(default=True)),
                ('clube', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipas', to='App.clube')),
            ],
        ),
        migrations.AddField(
            model_name='competicao',
            name='formato_competicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competicoes', to='App.formatocompeticao'),
        ),
    ]
