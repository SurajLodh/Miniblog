from django import forms
# from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Blogs

class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=10)
    # last_name = forms.CharField(max_length=10)
    # email = forms.EmailField(max_length=30)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email')
        labels = {'first_name':'First Name', 'last_name':'Last Name', 'email':'Email',}
        widgets = {
        'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_("password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['title','dis']
        labels = {'title':'Title','dis':'Description'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),'dis':forms.Textarea(attrs={'class':'form-control'})}

