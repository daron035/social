from django import forms

from .models import *

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': "Enter your email..."}),
        }
        labels = {
            'email': ''
        }