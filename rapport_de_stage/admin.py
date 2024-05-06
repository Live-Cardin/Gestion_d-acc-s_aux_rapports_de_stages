from django.contrib import admin
from .models import *

admin.site.register(Etudiant)

@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    list_display="user","niveau"

admin.site.register(Consultant)

@admin.register(Departement)
class DepartementAdmin(admin.ModelAdmin):
    list_display="nom","faculte","option"

@admin.register(Rapport)
class RapportAdmin(admin.ModelAdmin):
    list_display= "sujet","rapport_pdf","date_defendu","personnel","departement"
    search_fields="sujet",
    list_filter="departement",
    



