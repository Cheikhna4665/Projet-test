from django.contrib import admin
from .models import classe

# Register your models here.
@admin.register(classe)
class classeAdmin(admin.ModelAdmin):
    list_display=('id','name')