from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

class Conversation(models.Model):
    users = models.ManyToManyField(get_user_model())


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True, blank=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, null=True)
    
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description