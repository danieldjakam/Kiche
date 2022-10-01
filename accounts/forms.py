from operator import mod
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.utils.translation import gettext_lazy as _

class RegisterForm(UserCreationForm):
    username = forms.CharField(label=_('username'), widget=forms.TextInput(attrs={
        'class': 'for'
    }))
    email = forms.EmailField(label=_('email'))
    password1 = forms.CharField(label=_('password'), widget=forms.PasswordInput())
    password2 = forms.CharField(
        label=_('confirm a password'), widget=forms.PasswordInput()
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EditProfileForm(forms.ModelForm):
    subname = forms.CharField(
        label=_('prenom'), widget=forms.TextInput()
    )
    family_name = forms.CharField(
        label=_('nom de famille'), widget=forms.TextInput()
    )
    bio = forms.CharField(
        label=_('bio'), widget=forms.Textarea
    )
    site_web = forms.CharField(
        label=_('web site'), widget=forms.TextInput()
    )
    company = forms.CharField(
        label=_('company'), widget=forms.TextInput()
    )
    avatar = forms.ImageField(
        label=_('avatar'), widget=forms.FileInput(attrs={
            'class': 'imageChanger'
        })
    )
    is_a_proffessional_account = forms.BooleanField(
        label=_('is a professional account'), widget=forms.CheckboxInput()
    )
    class Meta:
        model = Profile
        fields = [ 'family_name', 'subname', 'site_web', 'company', 'bio', 'avatar', 'is_a_proffessional_account',]