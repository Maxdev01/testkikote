from django.contrib import admin

from .models import PlaceCategory, ArchivesPlace

# Register your models here.

@admin.register(PlaceCategory)
class PlaceCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ArchivesPlace)
class ArchivesPlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'categorie', 'created', 'email']
    prepopulated_fields = {'slug': ('name','categorie','adress',)}




    

