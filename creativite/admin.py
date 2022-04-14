from csv import list_dialects
from django.contrib import admin
from .models import CreationCategories, Texte , Commentaire, ArticlePost, UserIpText, categoriesPost, Reply , UserIp,UserIpText

# Register your models here.
admin.site.register(UserIp)
admin.site.register(UserIpText)


@admin.register(CreationCategories)
class CreationCategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Texte)
class TexteAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ['name','body']


@admin.register(ArticlePost)
class ArticlePostAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title', )}



@admin.register(categoriesPost)
class categoriesPostAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ['name', 'date']

    






