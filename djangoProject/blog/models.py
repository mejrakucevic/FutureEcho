from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    developer = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    release_date = models.DateField()
    image_link = models.URLField(max_length=255)
    exclusive = models.BooleanField(default=False)

    def __str__(self):
        return self.title


    
    
