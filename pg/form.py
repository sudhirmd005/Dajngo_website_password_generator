from django import forms
from .models import Pass_gen

class Pass_generator(forms.ModelForm):
    class Meta():
        model = Pass_gen
        fields = ['Full_name', 'Email_ID']
        
        widgets= {
            'Full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Full Name'}),
            'Email_ID': forms.EmailInput(attrs={'class' : 'form-control', 'placeholder':'Email ID'})
        }
