from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('email', 'username', 'first_name', 'last_name')


class LoginForm(forms.Form):
  username = forms.CharField(
    widget = forms.TextInput(
      attrs = {
        'class' : 'form-control',
        'placeholder' : 'Username'
      }
    )
  )

  password = forms.CharField(
    widget = forms.PasswordInput(
      attrs = {
        'class' : 'form-control',
        'placeholder' : 'Password'
      }
    )
  )