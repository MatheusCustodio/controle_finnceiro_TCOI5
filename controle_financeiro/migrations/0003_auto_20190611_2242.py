# Generated by Django 2.2.1 on 2019-06-11 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_financeiro', '0002_grupomodel_usuariogrupomodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariogrupomodel',
            name='data_cadastro',
            field=models.DateField(null=True, verbose_name='Data de Saida'),
        ),
    ]