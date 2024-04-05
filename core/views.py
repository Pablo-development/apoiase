from django.shortcuts import render


# Create your views here.

def str(request):
    return render(request, "index.html")


def index(request):
    useremail = None
    username = None
    userfone = None

    if request.method == 'POST':
        username = request.POST['username']
        useremail = request.POST['useremail']
        userfone = request.POST['userfone']

    return render(request, 'index.html', {'username': username, 'useremail': useremail, 'userfone': userfone})
