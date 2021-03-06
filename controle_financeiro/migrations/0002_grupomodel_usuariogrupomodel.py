# Generated by Django 2.2.1 on 2019-06-04 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controle_financeiro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoModel',
            fields=[
                ('grupo_id', models.AutoField(primary_key=True, serialize=False)),
                ('grupo_nome', models.CharField(max_length=45, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
                'ordering': ['grupo_nome'],
            },
        ),
        migrations.CreateModel(
            name='UsuarioGrupoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateField(verbose_name='Data de Saida')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle_financeiro.GrupoModel')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle_financeiro.UsuarioModel')),
            ],
            options={
                'verbose_name': 'UsuarioGrupo',
                'verbose_name_plural': 'UsuariosGrupos',
                'ordering': ['data_cadastro'],
                'unique_together': {('usuario', 'grupo')},
            },
        ),
    ]
