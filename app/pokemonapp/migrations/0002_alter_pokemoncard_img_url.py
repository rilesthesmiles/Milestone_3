# Generated by Django 4.1.4 on 2023-10-11 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemonapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemoncard',
            name='img_url',
            field=models.CharField(max_length=255),
        ),
    ]