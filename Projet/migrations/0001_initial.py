# Generated by Django 5.0 on 2023-12-11 13:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('besoin', models.IntegerField()),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('effectif', models.CharField(default='Manque', max_length=10)),
                ('type', models.CharField(choices=[('w', 'Web'), ('m', 'Mobile'), ('d ', 'Desktop')], default='Manque', max_length=10)),
                ('createur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projets_crees', to=settings.AUTH_USER_MODEL)),
                ('developpeurs', models.ManyToManyField(related_name='projets_developpes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Projet',
            },
        ),
        migrations.AddConstraint(
            model_name='projet',
            constraint=models.CheckConstraint(check=models.Q(('besion__gt', 0)), name="Please 'Besion' must be greater then 0"),
        ),
    ]
