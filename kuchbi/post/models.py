from django.db import models

# Create your models here.

class MyTable(models.Model):
    uname = models.CharField(max_length=20)
    pwd =models.CharField(max_length=100)

    def __str__(self):
        return self.uname