from django import forms
from .models import Restaurants

class ResForm(forms.ModelForm):
    class Meta:
        model = Restaurants
        fields = ['Res_name', 'Food_cat', 'img', 'address']