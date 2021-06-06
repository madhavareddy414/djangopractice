from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image= models.ImageField(default='default.jpg',upload_to='profile_pics.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'

class Posts(models.Model):
    title = models.CharField(max_length=64)
    author = models.OneToOneField(User,on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now())