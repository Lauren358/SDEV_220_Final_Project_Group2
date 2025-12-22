from django import forms
from .models import Inventory, Take

class DonoForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = {'food_name', 'food_total'}

class TakeForm(forms.ModelForm):
    class Meta:
        model = Take
        fields = ['name', 'food_name','food_total']
