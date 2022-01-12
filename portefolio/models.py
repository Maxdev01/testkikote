from django.db import models
from django.conf import settings

from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User 

from cloudinary.models import CloudinaryField

# Create your models here.

# Categorie for my projects
# for using 
#       profil
#       project
#       the jobs 

class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    
    # photo = models.ImageField(upload_to="image_files", null=True, blank=True)
    
    photo = CloudinaryField("image", null=True, blank=True)

    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=100,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    school = models.CharField(max_length=100,null=True, blank=True)
    universite = models.CharField(max_length=100, null=True, blank=True)
    profesional_school = models.CharField(max_length=100, null=True, blank=True)
    ville = models.CharField(max_length=100, null=True, blank=True)
    view = models.IntegerField(default=0)

    def __str__(self):
        return self.name 



class JobPerso(models.Model):
    categorie = models.ManyToManyField('Category', related_name='jobpersos', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobpersos')
    title = models.CharField(max_length=500)
    description = models.TextField()
    date_from = models.DateTimeField(default=timezone.now)
    date_to = models.DateField()
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone_1 = models.CharField(max_length=20)
    phone_2 = models.CharField(max_length=20, null=True, blank=True)
    ville = models.CharField(max_length=100)
    view = models.IntegerField(default=0)



    def __str__(self):
        return self.title


class JobEntreprise(models.Model):
    categorie = models.ManyToManyField('Category', related_name='jobentreprises', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobentreprises')
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    description = models.TextField()
    date_from = models.DateTimeField(default=timezone.now)
    date_to = models.DateField()
    email = models.EmailField()
    ville = models.CharField(max_length=200)
    adresse = models.CharField(max_length=250)
    phone_1 = models.CharField(max_length=20)
    phone_2 = models.CharField(max_length=20, null=True, blank=True)
    view = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# user project 
# part very important for this project 

class ProjectUser(models.Model):
    categorie = models.ManyToManyField('Category', related_name='projectusers')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    slug = models.SlugField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=500)
    description = models.TextField()
    mail = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15, null=True, blank=True)
    experience = models.TextField(null=True, blank=True)
    like = models.IntegerField(default=0)
    eyes = models.IntegerField(default=0)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


   