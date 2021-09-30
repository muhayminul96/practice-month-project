from django.db import models
from datetime import datetime


# Create your models here.

class Room(models.Model):
    room_name = models.CharField(max_length=100)

    def __str__(self):
        return self.room_name


class Text(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    text = models.CharField(max_length=5000)
    username = models.CharField(max_length=200)

    def __str__(self):
        return str(self.date)
