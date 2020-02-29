from django.db import models

# Create your models here.

class Likes(models.Model):
    like= models.IntegerField()

    