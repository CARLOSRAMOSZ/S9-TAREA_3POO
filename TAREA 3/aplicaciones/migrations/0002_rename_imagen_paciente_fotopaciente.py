# Generated by Django 4.1.7 on 2023-03-01 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='imagen',
            new_name='FotoPaciente',
        ),
    ]
