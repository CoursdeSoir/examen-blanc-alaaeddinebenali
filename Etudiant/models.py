from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


def Verif_username(value):
    if not str(value).startswith("ing"):
        raise ValidationError(f"{value}Il faut qu'il commence par 'ing' !")
    return value


class Etudiant(AbstractUser):
    username = models.CharField(max_length=255, unique=True, primary_key=True, validators=[Verif_username])
    classe = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=24, null=False)

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'Etudiant'

    def __str__(self):
        return self.username
