# Generated by Django 3.1.7 on 2021-12-04 03:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreationCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Texte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('publier_by', models.CharField(max_length=100)),
                ('view', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique_for_date='date')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(default=True)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='textes', to='creativite.creationcategories')),
            ],
        ),
    ]
