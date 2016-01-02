from django.contrib.auth.hashers import make_password

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect
from .models import User
from .forms import RegisterForm, SiginForm

import datetime

def home(request):
    if 'user_id' in request.COOKIES:
        return HttpResponseRedirect('/whatsapp/')
    else:
        if len(User.objects.all()) == 0:
            return redirect('register')
        else:
            return redirect('sigin')

def sigin(request):
    if request.method == 'POST':
        form = SiginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = User.objects.get(username=username)
            response = HttpResponseRedirect('/whatsapp/')
            response.set_cookie('user_id', user.id)
            return response
        else:
            return render(request, 'accounts/form.html',
                        {'form': form,
                        'title': 'Ingrese sus datos de usuario',
                        'url': '/accounts/sigin/'})
    else:
        form = SiginForm()
        return render(request, 'accounts/form.html',
                      {'form': form,
                       'title': 'Ingrese sus datos de usuario',
                       'url': '/accounts/sigin/'})

def logout(request):
    try:
        response = HttpResponseRedirect('/')
        response.delete_cookie('user_id')
        return response
    except KeyError:
        pass
    return HttpResponseRedirect('/')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user = User(username=username,
                        password=make_password(password, hasher='pbkdf2_sha256'),
                        email=email,
                        date_joined=datetime.datetime.now())
            user.save()
            return HttpResponseRedirect('/whatsapp/')
        else:
            return render(request, 'accounts/form.html',
                        {'form': form,
                        'title': 'Registre sus datos en el sistema',
                        'url': '/accounts/register/'})
    else:
        form = RegisterForm()
        return render(request, 'accounts/form.html',
                      {'form': form,
                       'title': 'Registre sus datos en el sistema',
                       'url': '/accounts/register/'})

