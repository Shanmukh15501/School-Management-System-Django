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
        fields=['email','phone','first_name','last_name','state','city','address','department','role','password1','password2']



class UserAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'autofocus': True,'class':'form-control',"placeholder":"Email/Username"},))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control',"placeholder":"Enter Password"},))
