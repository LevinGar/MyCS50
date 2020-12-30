from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Profile(models.Model):
    target = models.ForeignKey('User', on_delete=models.CASCADE, related_name='folowers')
    follower = models.ForeignKey('User', on_delete=models.CASCADE, related_name='targets')

class Post(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='author')
    content = models.CharField(max_length=255)
    address = models.CharField(max_length=100,default="No direccion")
    date = models.DateTimeField(default=datetime.now())
    liked = models.ManyToManyField('User', default=None, blank=True, related_name='post_likes')
    lat = models.FloatField()
    lng = models.FloatField()
    requester = models.CharField(max_length=25,default="Unknown")

    @property
    def num_likes(self):
        return self.liked.all().count()


class Like(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)


    def __str__(self):
        return str(self.post)
