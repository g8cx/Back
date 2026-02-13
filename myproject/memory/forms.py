from django import forms
from .models import Fallen

class FallenForm(forms.ModelForm):
    class Meta:
        model = Fallen
        fields = ['name', 'birth_year', 'death_year', 'description']