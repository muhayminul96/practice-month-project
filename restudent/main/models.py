from django.db import models

# Create your models here.

class Table(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=40)
    submitTime = models.DateTimeField(auto_now_add=True)
    date = models.CharField(max_length=40)
    time = models.CharField(max_length=40)
    numberOfPeople = models.IntegerField()
    message = models.TextField()




    def __str__(self):

        return self.name

class Contract(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='media')
    details = models.TextField()

    def __str__(self):
        return self.name


class Items(models.Model):
    Category_Choice = [
        ('starters', 'Starters'),
        ("salads", 'Salads'),
        ('specialty', 'Specialty'),
    ]


    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    category = models.CharField(max_length=100,choices=Category_Choice)
    details = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name