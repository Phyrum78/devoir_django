# Generated by Django 5.0.4 on 2024-04-10 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GestionRecettes', '0002_rename_étapes_recette_etapes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recette',
            old_name='incredients',
            new_name='ingredients',
        ),
    ]
