# Generated by Django 4.2.16 on 2024-11-10 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_remove_competicao_vencedores_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('ano', models.IntegerField()),
            ],
        ),
    ]
