from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmailForm(forms.Form):
    email = forms.EmailField()

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'USERNAME'}))
    email=forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'EMAIL ADDRESS'}), max_length=254)
    password1=forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'PASSWORD'}))
    password2=forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'CONFIRM PASSWORD'}))


    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)
        
        