# Generated by Django 5.0 on 2023-12-12 19:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projet', '0003_developpeur'),
    ]

    operations = [
        migrations.AddField(
            model_name='developpeur',
            name='date_adhesion',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2023, 12, 12, 20, 15, 24, 699342)),
        ),
    ]
