# Generated by Django 3.1.7 on 2021-10-13 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portefolio', '0012_jobentreprise_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectuser',
            name='categorie',
            field=models.ManyToManyField(blank=True, to='portefolio.Category'),
        ),
    ]
