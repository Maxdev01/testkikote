# Generated by Django 3.1.7 on 2022-01-12 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creativite', '0003_commentaire_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='texte',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='image_files'),
        ),
    ]
