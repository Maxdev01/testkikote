from email.policy import default
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User 

from cloudinary.models import CloudinaryField


# Create your models here.


class CreationCategories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)


    def __str__(self):
        return self.name 


class Texte(models.Model):
    categorie = models.ForeignKey(CreationCategories, related_name="textes", on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    email = models.CharField(max_length=100, null=True, blank=True)
    # photo = models.ImageField(upload_to="image_files", null=True, blank=True)

    photo = CloudinaryField("image", null=True, blank=True)

    text = models.TextField()
    author = models.CharField(max_length=100)
    publier_by = models.CharField(max_length=100)
    view = models.IntegerField(default=0)
    slug = models.SlugField(unique_for_date='date')
    date = models.DateTimeField(default= timezone.now)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.title


class Commentaire(models.Model):
    post = models.ForeignKey(Texte, on_delete=models.CASCADE, related_name='mycoms')
    name = models.CharField(max_length=100, null=True, blank=100)
    body = models.CharField(max_length=800)

    def __str__(self):
        return self.name 
        



class categoriesPost(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)


    def __str__(self):
        return self.name 


class ArticlePost(models.Model):
    category = models.ForeignKey(categoriesPost, related_name="articleposts", on_delete=models.CASCADE)
    title = models.CharField(max_length=900)
    sub_title = models.CharField(max_length=500, null=True, blank=True)
    author = models.CharField(max_length=300)
    date_created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique_for_date="date_created")
    body = models.TextField()
    photho1 = models.ImageField(upload_to="image_files")
    photho2 = models.ImageField(upload_to="image_files", null=True, blank=True)
    publish_by = models.CharField(max_length=200)
    like = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    mail = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.title


