from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewBookForm(forms.Form):
        title=forms.CharField(label='Title',max_length=100)
        price=forms.FloatField(label='Price')
        author=forms.CharField(label='Author')
        publisher=forms.CharField(label='Publisher')

class SearchForm(forms.Form):
      title=forms.CharField(label='Title',max_length=100)

class UserRegisterForm(UserCreationForm):
    mobile=forms.CharField()
    class Meta:
        model=User
        fields=['first_name','last_name','mobile','email','username','password1','password2']
