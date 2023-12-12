from django.urls import path
from .views import listProject

urlpatterns = [
    path('list', listProject, name="listProjets"),
    path('', listProject, name="listProjets"),
]
