from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class signUpForm(UserCreationForm):
    email=forms.CharField(max_length=255,required=True,widget=forms.EmailInput)
    first_name=forms.CharField(max_length=150,required=True)
    last_name=forms.CharField(max_length=150,required=True)

    class Meta:
        model=User
        fields={'email','last_name','password2','password1','first_name','username'}
