from django import forms
from django.contrib.auth.forms import AuthenticationForm,BaseUserCreationForm
from django.utils.translation import gettext_lazy,gettext as _
from CustomUser.models import *
from django.db.models import Q
from django.contrib.auth import (authenticate,get_user_model)
from django.contrib.auth.forms import *


class UserRegistrationForm(BaseUserCreationForm):
    class Meta:
        model=Users
        fields=['email','phone','first_name','last_name','standard','section','gender','DOB','state','city','address','department','role','password1','password2']
        # css changes
        widgets = {
            'email': forms.EmailInput(attrs={ 'class' : 'form-control'}),
            'first_name': forms.TextInput(attrs={ 'class' : 'form-control 1'}),
            'password1': forms.TextInput(attrs={ 'class' : 'form-control'}),
            'password2': forms.TextInput(attrs={ 'class' : 'form-control'}),
            'last_name': forms.TextInput(attrs={ 'class' : 'form-control'}),
            'DOB': forms.DateInput(attrs={ 'class' : 'form-control'}),
            'phone': forms.TextInput(attrs={'class' : 'form-control'}),
            'standard': forms.Select(attrs={'class' : 'form-control'}),
            'section': forms.Select(attrs={'class' : 'form-control'}),
            'gender': forms.Select(attrs={'class' : 'form-control'}),
            'state': forms.Select(attrs={'class' : 'form-control'}),
            'city': forms.Select(attrs={'class' : 'form-control'}),
            'department': forms.Select(attrs={'class' : 'form-control'}),
            'role': forms.Select(attrs={'class' : 'form-control'}),
            'address': forms.Textarea(attrs={'class' : 'form-control'}),
        }



class UserAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'autofocus': True,'class':'form-control',"placeholder":"Email/Username"},))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control',"placeholder":"Enter Password"},))
