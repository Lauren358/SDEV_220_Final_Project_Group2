from django import forms
from .models import Inventory

class DonoForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = {'food_name', 'food_total'}

