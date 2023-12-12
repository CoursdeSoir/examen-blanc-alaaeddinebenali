from django.contrib import admin

from .models import Projet


@admin.display(description="projet")
def displayTxt(obj):
    return f"Projet avec l'identifiant {obj.id} a besoin de {obj.besoin} étudiant(s)"

class TypeListFilter(admin.SimpleListFilter):
    title = "By Type de projet et effectif"
    parameter_name = 'type'

    def lookups(self, request, model_admin):
        return (
            ('Web', ('Projet Web')),
            ('Mobile', ('Projet Mobile')),
            ('Desktop', ('Projet Desktop')),
            ('Manque_effectif', ('Projet sans effectif'))
        )

    def queryset(self, request, queryset):
        if self.value() == 'Web':
            return queryset.filter(type__exact="w")
        if self.value() == 'Mobile':
            return queryset.filter(type__exact="m")
        if self.value() == 'Desktop':
            return queryset.filter(type__exact="d")
        if self.value() == 'Manque_effectif':
            return queryset.filter(effectif__exact="Manque")


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    search_fields = ["createur"]
    autocomplete_fields = ['createur']

    fieldsets = (
        ('A propos', {"fields": ('besoin', 'effectif')}),
        ('Date', {"fields": ('date_debut', 'date_fin')}),
        ('Categorie', {"fields": ('type',)}),
        ('Equipe', {"fields": ('createur',)})
    )

    list_filter = (TypeListFilter,)


admin.register(Projet, ProjetAdmin)
