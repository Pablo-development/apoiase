from django.shortcuts import render



# Create your views here.

def index(request):

    username = None
    userfone = None
    useremail = None

    if request.method == 'POST':
        username = request.POST['username']
        useremail = request.POST['useremail']
        userfone = request.POST['userfone']

    return render(request, "index.html", {'username': username, 'userfone': userfone, 'useremail': useremail})


def cadastro_clientes(request):
    return render(request, 'cadastro_clientes.html')


def duvidas_frequentes(request):
    return render(request, 'duvidas_frequentes.html')


