from django.db import models

# Create your models here.

class Message(models.Model):
    description = models.TextField(null=True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)