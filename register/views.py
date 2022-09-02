from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(response):
  if response.method == "POST":
    form = RegistrationForm(response.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(response, f'account created for {username}! WELCOME')
      
      return redirect("login")

  else:
    form = RegistrationForm()


  return render(response, "register.html", {"form":form})


def login(response):
  if response.method == "POST":
    l_form = LoginForm(response.POST)
    if l_form.is_valid():
      l_form.save()

    return redirect("/")

  else:
    l_form = LoginForm()


  return render(response, "login.html", {"l_form":l_form})

@login_required
def profile(request):
  return render(request, "profile.html")