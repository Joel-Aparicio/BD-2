# Generated by Django 3.2.25 on 2024-11-23 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_equipa'),
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
    ]
