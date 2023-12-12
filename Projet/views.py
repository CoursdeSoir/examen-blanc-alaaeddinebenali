from django.shortcuts import render

from .models import Projet


# Create your views here.
def listProject(req):
    list = Projet.objects.all().order_by('date_debut')
    return render(req, 'Projet/list.html', {'projects': list})
