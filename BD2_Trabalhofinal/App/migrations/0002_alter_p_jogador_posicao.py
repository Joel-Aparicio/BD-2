# Generated by Django 3.2.25 on 2024-12-22 17:13

from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='p_jogador',
            name='posicao',
            field=djongo.models.fields.JSONField(blank=True, null=True),
        ),
    ]
