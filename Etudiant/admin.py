from django.contrib import admin

from .models import Etudiant


@admin.register(Etudiant)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "classe")
    search_fields = ["username"]
