# Generated by Django 3.1.7 on 2021-12-10 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0002_auto_20211111_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archivesplace',
            name='time_close',
        ),
        migrations.RemoveField(
            model_name='archivesplace',
            name='time_open',
        ),
        migrations.AlterField(
            model_name='archivesplace',
            name='image_one',
            field=models.ImageField(blank=True, null=True, upload_to='archives_images'),
        ),
    ]
