# Generated by Django 3.2.25 on 2024-11-19 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_auto_20241119_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='competicao',
            name='formato_competicao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='competicoes', to='App.formatocompeticao'),
        ),
    ]
