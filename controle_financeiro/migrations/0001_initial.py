# Generated by Django 2.2.1 on 2019-05-27 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioModel',
            fields=[
                ('usuario_id', models.AutoField(primary_key=True, serialize=False)),
                ('usuario_nome', models.CharField(max_length=45, verbose_name='Nome')),
                ('usuario_email', models.CharField(max_length=45, verbose_name='Email')),
                ('usuario_senha', models.CharField(max_length=45, verbose_name='Senha')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'ordering': ['usuario_nome'],
            },
        ),
    ]
