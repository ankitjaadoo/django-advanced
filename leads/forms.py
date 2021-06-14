from leads.models import Lead
from django import forms
from django.contrib.auth import get_user_model
from .models import Lead, User
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
        )

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        fields_classes = {'username': UsernameField}

class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)
    
