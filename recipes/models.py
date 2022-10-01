from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    creator = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Creator')
    name = models.CharField(max_length=255, verbose_name='Name of recipe')
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name='Description of recipe')
    nbre_of_plates = models.IntegerField(verbose_name='Number of plates of recipe')
    time_preparation = models.IntegerField(verbose_name='Time of preparation of recipe')
    time_cuisson = models.IntegerField(null=True, blank=True, verbose_name='Time of cuisson of recipe')
    status = models.CharField(max_length=255, default='public', verbose_name='Status of recipe')
    ingredients = models.TextField()
    preparation_step = models.TextField()
    cuisson_step = models.TextField()
    picture = models.ImageField(null=True, blank=True, upload_to='recipes_picture/')
    created_at = models.DateField(auto_now_add=True)