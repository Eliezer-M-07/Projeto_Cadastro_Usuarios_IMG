# Generated by Django 4.1.7 on 2023-07-28 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro_users', '0002_usuario_delete_usuarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='arq',
            field=models.FileField(upload_to='media'),
        ),
    ]
