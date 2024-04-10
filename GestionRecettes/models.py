from django.db import models

# Create your models here.
class Recette(models.Model):
    nomRecette = models.CharField(max_length=100)
    ingredients = models.TextField(max_length=1000)
    etapes = models.TextField()
    author = models.CharField(max_length=100)
    imageURL = models.URLField(max_length=200, null=True, blank=True)
    notes = models.TextField(max_length=1000, null=True, blank=True) 
