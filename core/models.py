from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.
AGE_CHOICES=(
    ('All', 'All'),
    ('Kids', 'Kids')
)
MOVIE_TYPE=(
    ('single', 'Single'),
    ('seasonal', 'Seasonal')
)

class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile')
    
    


class Profile(models.Model):
    name = models.CharField(max_length=100)
    age_limit = models.CharField(max_length=20, choices=AGE_CHOICES)    
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    
    def __str__(self):
        return self.name +" "+self.age_limit


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    type = models.CharField(max_length=20, choices=MOVIE_TYPE)
    videos = models.ManyToManyField('Video')
    flyer = models.ImageField(upload_to='flyers', blank=True, null=True)
    age_limit = models.CharField(max_length=20, choices=AGE_CHOICES)
     
    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='movies')  

    def __str__(self):
        return self.title 
