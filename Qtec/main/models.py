from django.db import models
from django.contrib.auth.models import User

class SearchHistory(models.Model):

    keyword = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.keyword

