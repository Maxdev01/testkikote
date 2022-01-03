from django.contrib import admin
from .models import Profile , JobEntreprise, JobPerso , ProjectUser , Category
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']

@admin.register(JobEntreprise)
class JobEntrepriseAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'date_from', 'date_to']


@admin.register(JobPerso)
class JobPersoAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_from', 'date_to', 'ville']


@admin.register(ProjectUser)
class ProjectUserAdmin(admin.ModelAdmin):

    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}