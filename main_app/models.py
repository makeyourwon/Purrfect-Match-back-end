from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import json

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  age = models.IntegerField(null=True, blank=True)
  location = models.CharField(max_length=50)
  phone = models.CharField(null=True, blank=True)
  favorites = models.OneToOneField('Favorite', on_delete=models.CASCADE, null=True, blank=True, related_name='profile')
  #add user model here
  def __str__(self):
    return str(self.id)
  

class Animal(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    breed = models.JSONField(default=dict)
    age = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    gender = models.CharField(max_length=100)
    color = models.JSONField(default=dict)
    status = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=250, null=True, blank=True)
    photos = models.JSONField(default=list)
    contact = models.JSONField(default=dict)

    def __str__(self):
     return self.name

class Favorite(models.Model):
    animals = models.ManyToManyField(Animal)

    def __str__(self):
        # return ', '.join([animal.name for animal in self.animals.all()])
        return f" {self.id}"
