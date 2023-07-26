from django import forms
from .models import ComplaintsData
from django.core import validators

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = ComplaintsData
        fields = ['name', 'email', 'complaintAgainst', 'complaintDetails']
        widgets = {
            'name': forms.TextInput(attrs={ 'class' : 'form-control'}),
            'email': forms.EmailInput(attrs={'class' : 'form-control'}),
            'complaintAgainst': forms.Select(attrs={'class' : 'form-control'}),
            'complaintDetails': forms.Textarea(attrs={'class' : 'form-control'})
        }