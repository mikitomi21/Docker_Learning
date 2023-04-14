from django.forms import ModelForm
from django.http import request

from .models import Message, Room
from django import forms
from django.contrib.auth.models import User
from django.forms import CheckboxSelectMultiple

class MessageForm(ModelForm):
    
    class Meta:
        model = Message
        fields = ['description']

class RoomForm(forms.ModelForm):

    def __init__(self, admin, *args, **kwargs):
        self.admin = admin
        super(RoomForm, self).__init__(*args, **kwargs)
        self.fields['members'].queryset = User.objects.exclude(username=admin.username)

    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=CheckboxSelectMultiple
    )

    class Meta:
        model = Room
        fields = ['name', 'members']