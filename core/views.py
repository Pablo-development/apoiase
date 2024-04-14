from django.shortcuts import render
from core.models import models, Pessoa
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse



# Create your views here.

def index(request):
    return render(request, "index.html")


def fazer_login(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponse("Você está logado!")
        else:
            return render(request, 'fazer_login.html')
    return render(request, 'fazer_login.html')


def cadastro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # criação de novo usuario para autenticação
        User.objects.create_user(username=username, email=email, password=request.POST['password'])
        return redirect('login')
    else:
        return render(request, 'cadastro.html')


def duvidas_frequentes(request):
    return render(request, 'duvidas_frequentes.html')
