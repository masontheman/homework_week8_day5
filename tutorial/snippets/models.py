from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    title = models.CharField(max_length=80)
    thumb = models.ImageField(upload_to='thumbnails/')
    video = models.FileField(upload_to='videos/')
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    desc = models.TextField(max_length=5000)
    
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    
    pub_date = models.DateTimeField(auto_now_add=True)
    
    