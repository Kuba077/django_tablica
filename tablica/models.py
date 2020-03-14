from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Post(models.Model):
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=1024)
    data_dodania = models.DateField()

    def __str__(self):
        return self.uzytkownik.username + ': ' + self.text
