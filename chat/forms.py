from django.forms import ModelForm
from .models import Message, Room
from django import forms
from django.contrib.auth.models import User
from django.forms import CheckboxSelectMultiple

class MessageForm(ModelForm):
    
    class Meta:
        model = Message
        fields = ['description']

class RoomForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=CheckboxSelectMultiple
    )

    class Meta:
        model = Room
        fields = ['name', 'members']