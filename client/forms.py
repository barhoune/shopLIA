from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

class SignupForm(forms.Form):
    username = forms.CharField(max_length=150)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    address = forms.CharField(max_length=255)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], widget=forms.RadioSelect)