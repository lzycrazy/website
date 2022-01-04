from collections import defaultdict
from typing import DefaultDict
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.expressions import Value 
from django.utils.timezone import now 
    
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='images')
    content = models.TextField()
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    

    def __str__(self):
        return self.title

class Carausel(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title   


class About(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    subtitle = models.CharField(max_length=150)
    content = models.TextField()

    def __str__(self):
        return self.title 
        

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    content = models.TextField()
    

    def __str__(self):
        return 'Message from' + self.name  + ' - ' + self.email



class News(models.Model):
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.email


class Gallery(models.Model):
    video = models.FileField(upload_to='video/%Y')
    photo1 = models.ImageField(upload_to='images')
    photo2 = models.ImageField(upload_to='images')