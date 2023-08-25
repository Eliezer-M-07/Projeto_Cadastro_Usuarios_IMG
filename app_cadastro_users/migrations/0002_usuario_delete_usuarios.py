# Generated by Django 4.1.7 on 2023-07-26 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('idade', models.IntegerField()),
                ('cpf', models.IntegerField()),
                ('arq', models.FileField(upload_to='img')),
            ],
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
    ]
