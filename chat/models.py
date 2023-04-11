from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=200,null=True)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description