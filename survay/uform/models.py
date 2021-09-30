from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=300)
    gender = models.CharField(max_length=30)
    department = models.CharField(max_length=30)

