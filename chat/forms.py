from django.forms import ModelForm
from .models import Message, Room
from django import forms
from django.contrib.auth.models import User

class MessageForm(ModelForm):
    
    class Meta:
        model = Message
        fields = ['description']

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ['name', 'members']