from django.forms import ModelForm
from .models import User

class ConnectForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']