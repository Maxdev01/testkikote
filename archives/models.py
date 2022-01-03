from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 


# Create your models here.



class PlaceCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.name


class ArchivesPlace(models.Model):
    categorie = models.ForeignKey(PlaceCategory, related_name='archives', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    name = models.CharField(max_length=500)
    image_one = models.ImageField(upload_to="archives_images", null=True, blank=True)
    image_two = models.ImageField(upload_to="archives_images", null=True, blank=True)
    adress = models.CharField(max_length=500)
    phone_one = models.CharField(max_length=15)
    phone_two = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True )
    description = models.TextField(null=True, blank=True)
    website_link = models.CharField(max_length=500, null=True, blank=True)
    website_link_second = models.CharField(max_length=500, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique_for_date='created')
    views = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.name


    class Meta:
        ordering = ['-created']

    

