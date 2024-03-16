from django.contrib import admin
from .models import etud

# Register your models here.

@admin.register(etud)
class etudAdmin(admin.ModelAdmin):
    list_display = ('id','code','name','prenom','N_Tel','classe')