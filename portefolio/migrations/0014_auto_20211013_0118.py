# Generated by Django 3.1.7 on 2021-10-13 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portefolio', '0013_auto_20211013_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='jobentreprise',
            name='categorie',
            field=models.ManyToManyField(related_name='jobentreprises', to='portefolio.Category'),
        ),
        migrations.AlterField(
            model_name='jobperso',
            name='categorie',
            field=models.ManyToManyField(related_name='jobpersos', to='portefolio.Category'),
        ),
        migrations.AlterField(
            model_name='projectuser',
            name='categorie',
            field=models.ManyToManyField(related_name='projectusers', to='portefolio.Category'),
        ),
    ]
