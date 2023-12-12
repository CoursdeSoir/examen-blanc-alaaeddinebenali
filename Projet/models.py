import datetime

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

from Etudiant.models import Etudiant


class Projet(models.Model):
    type_list = (
        ("w", "Web"),
        ("m", "Mobile"),
        ("d ", "Desktop"),
    )

    id = models.AutoField(primary_key=True)
    besoin = models.IntegerField(null=False)
    date_debut = models.DateField(null=False)
    date_fin = models.DateField(null=False)
    effectif = models.CharField(max_length=10, default="Manque")
    type = models.CharField(max_length=10, choices=type_list, default="Manque")
    developpeurs = models.ManyToManyField(Etudiant, related_name='projets_developpes')
    createur = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='projets_crees')

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'Projet'
        constraints = [
            models.CheckConstraint(check=models.Q(
                besoin__gt=0
            ), name="Please 'Besion' must be greater then 0")
        ]

    def __str__(self):
        return f'Projet avec l\'identifiant {self.id} a besoin de {self.besoin} étudiant(s)'


class Developpeur(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    date_adhesion = models.DateField(datetime.datetime.now(), null=True, auto_now_add=True)

    unique_together = [['etudiant', 'projet']]
