# Generated by Django 4.1.7 on 2023-03-01 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Paciente', models.CharField(max_length=250)),
                ('imagen', models.ImageField(null=True, upload_to='imagenes', verbose_name='Imagen')),
                ('Descripcion', models.TextField(null=True, verbose_name='Descripcion')),
            ],
        ),
    ]
