# Generated by Django 3.1.7 on 2021-12-06 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creativite', '0002_commentaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire',
            name='name',
            field=models.CharField(blank=100, max_length=100, null=True),
        ),
    ]