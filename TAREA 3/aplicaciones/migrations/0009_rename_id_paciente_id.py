# Generated by Django 4.1.7 on 2023-03-02 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0008_rename_id_paciente_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='id',
            new_name='ID',
        ),
    ]
