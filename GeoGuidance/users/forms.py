from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

class UserForm(UserCreationForm):
    fname = forms.CharField(max_length=30, required=True,
            widget=forms.TextInput(attrs={'placeholder': 'Enter first name'}))
    lname = forms.CharField(max_length=30, required=True,
            widget=forms.TextInput(attrs={'placeholder': 'Enter last name'}))
    username = forms.CharField(max_length=256, required=True,
            widget=forms.TextInput(attrs={'placeholder': 'Enter email name'}))
    password1 = forms.CharField(max_length=30, required=True,
            widget=forms.PasswordInput(attrs={'class': 'password', 'placeholder': 'Enter first name'}))
    password2 = forms.CharField(max_length=30, required=True,
            widget=forms.PasswordInput(attrs={'class': 'password', 'placeholder': 'Enter first name'}))

    token = forms.CharField(widget=forms.HiddenInput())
    
    class Meta:
        model = User
        fields = ('username','fname','lname','password1','password2')


class AuthForm(AuthenticationForm):
    username = forms.EmailField(max_length=256,required=True,
                widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField( widget=forms.PasswordInput(attrs={'placement':'Password','class':'password'}))
    
    class Meta:
        model = User
        field = ('username','password')
        
    
    
    
    

class UserProfileForm(forms.ModelForm):
    
    address = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    town = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    county = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    post_code = forms.CharField(max_length=8, required=True, widget=forms.HiddenInput())
    country = forms.CharField(max_length=40, required=True, widget=forms.HiddenInput())
    longitude = forms.CharField(max_length=50, required=True, widget=forms.HiddenInput())
    latitude = forms.CharField(max_length=50, required=True, widget=forms.HiddenInput())
    
    class Meta:
        model = UserProfile
        fields = ('address','town','county','post_code',
                  'country','longitude','latitude')