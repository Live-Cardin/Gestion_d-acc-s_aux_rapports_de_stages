from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib.auth import login, authenticate  # import des fonctions login et authenticate

from django import forms
from .models import Rapport

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'connection.html', context={'form': form, 'message': message})

def index(request):
    return render(request,"index.html",locals())


def rapport_list(request):
    rapports=Rapport.objects.all()
    return render(request,'home.html',{'rapports':rapports})


def home(request):
    if request.method=='POST':
        form=Rapport_form(request.POST)
        if form.is_valid():
                rapport=form.save(commit=False)
                rapport.save()
                return redirect('/home')
    else:
        form=Rapport_form()
        return render(request,'home.html',{'form':form})