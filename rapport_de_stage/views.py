from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib.auth import login, authenticate  # import des fonctions login et authenticate

from django import forms

from .forms import RapportForm
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



def rapport_create(request):
    if request.method == 'POST':
        form = RapportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('rapport_list')
    else:
        form = RapportForm()
    return render(request, 'rapport_form.html', {'form': form})

def rapport_list(request):
    rapports = Rapport.objects.all()
    return render(request, 'rapport_list.html', {'rapports': rapports})