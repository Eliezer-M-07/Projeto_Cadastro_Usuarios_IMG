# Generated by Django 4.1.7 on 2023-07-28 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro_users', '0004_alter_usuario_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.TextField(max_length=11),
        ),
    ]
