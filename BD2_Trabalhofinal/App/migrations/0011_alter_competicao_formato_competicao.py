# Generated by Django 3.2.25 on 2024-11-19 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_auto_20241119_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competicao',
            name='formato_competicao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='competicoes', to='App.formatocompeticao'),
        ),
    ]
