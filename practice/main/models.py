from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=500)

    def __str__(self):
        return self.name
