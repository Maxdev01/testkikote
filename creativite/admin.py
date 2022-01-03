from django.contrib import admin
from .models import CreationCategories, Texte , Commentaire

# Register your models here.


@admin.register(CreationCategories)
class CreationCategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Texte)
class TexteAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ['body']







