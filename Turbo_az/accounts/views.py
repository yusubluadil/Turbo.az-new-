from django.shortcuts import render, redirect
from .models import User
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def user_register(request):
  form = UserCreationForm()

  if (request.method == 'POST'):
    form = UserCreationForm(request.POST)

    if (form.is_valid()):
      form.save()
      return redirect("user_login")
  
  context = {
    'form' : form
  }

  return render(request, 'register.html', context)


def user_login(request):
  if (request.method == "POST"):
    form = AuthenticationForm(request, data = request.POST)

    if(form.is_valid()):
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username = username, password = password)

      if (user is not None):
        login(request, user)
        messages.info(request, f"You are now logged in as {username}.")
        return redirect('index')
      
      else:
        messages.error(request, "Invalid username or password.")
    
    else:
      messages.error(request, "Invalid username or password.")
  
  form = AuthenticationForm()
  context = {
    'form' : form
  }

  return render(request, "login.html", context)


def user_logout(request):
  logout(request)
  messages.info(request, "You have successfully logged out.")
  return redirect("user_login")
