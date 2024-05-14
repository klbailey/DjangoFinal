# finalAssessment>myapp>forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class RegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ['name', 'username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class TravelPlanForm(forms.ModelForm):
    class Meta:
        model = TravelPlan
        fields = ['destination', 'description', 'travel_date_from', 'travel_date_to']
