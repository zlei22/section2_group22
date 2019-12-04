from django import forms
from .models import Sighting

class SquirrelForm(forms.ModelForm):
    class Meta:
        model = Sighting
        fields = '__all__'
