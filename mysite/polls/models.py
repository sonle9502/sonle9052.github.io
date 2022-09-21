from pyexpat import model
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField( max_length=200)
    content= models.CharField( max_length=400)

