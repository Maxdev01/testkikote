# Generated by Django 4.0.3 on 2022-04-16 14:04

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creativite', '0011_alter_userip_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='photho1',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='photho2',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
