# Generated by Django 4.1.7 on 2023-07-28 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro_users', '0005_alter_usuario_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='arq',
            field=models.FileField(upload_to=''),
        ),
    ]
