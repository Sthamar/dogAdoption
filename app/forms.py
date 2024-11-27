from django import forms
from app.models import Adopter

class AdoptationForm(forms.ModelForm):
    class Meta:
        model = Adopter
        fields = ['first_name', 'last_name', 'contact_number', 'address']
        widgets = {
            'first_name':forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Last Name'}),
            'contact_number':forms.TextInput(attrs={'placeholder':'Contact Number'}),
            'address':forms.TextInput(attrs={'placeholder':'Address'}),
        }