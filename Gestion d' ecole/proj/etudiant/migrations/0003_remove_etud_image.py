# Generated by Django 5.0.1 on 2024-03-09 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etudiant', '0002_etud_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etud',
            name='image',
        ),
    ]
