# Generated by Django 5.0.4 on 2024-05-02 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapport_de_stage', '0003_departement_etudiant_departement_rapport_departement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departement',
            name='faculte',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='departement',
            name='nom',
            field=models.CharField(max_length=60),
        ),
    ]