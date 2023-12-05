from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from servicos.models import OrdemDeServico

def login_usuario(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = authenticate(username=username,password=senha)

        if user:
            login(request, user)
            return redirect('usuarios:home')
        else:
            return HttpResponse('email ou senha invalidos')

def home(request):
    ordens = OrdemDeServico.objects.all()
    conta_ordens = ordens.count()
    return render(request,'home.html', {'ordens':ordens, 'conta_ordens':conta_ordens})
