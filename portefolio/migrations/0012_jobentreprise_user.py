# Generated by Django 3.1.7 on 2021-10-13 00:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portefolio', '0011_remove_jobentreprise_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobentreprise',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='jobentreprises', to='auth.user'),
            preserve_default=False,
        ),
    ]
