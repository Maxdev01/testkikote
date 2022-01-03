# Generated by Django 3.1.7 on 2021-10-13 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portefolio', '0014_auto_20211013_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobentreprise',
            name='categorie',
            field=models.ManyToManyField(blank=True, null=True, related_name='jobentreprises', to='portefolio.Category'),
        ),
        migrations.AlterField(
            model_name='jobperso',
            name='categorie',
            field=models.ManyToManyField(blank=True, null=True, related_name='jobpersos', to='portefolio.Category'),
        ),
    ]
