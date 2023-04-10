from django.forms import ModelForm
from django.contrib.auth.models import User

class EditForm(ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
