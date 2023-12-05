from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Mecanico, Equipe


def cadastro_mecanico(request):
    if request.method == 'POST':
        if 'cancelar' in request.POST:
            return redirect('usuarios:home')
        else:
            novo_mecanico = Mecanico()
            novo_mecanico.nome = request.POST.get('nome')
            novo_mecanico.especialidade = request.POST.get('especialidade')
            novo_mecanico.save()
            return redirect('usuarios:home')
    return render(request, 'cadastro_mecanico.html')


def cadastro_equipe(request):
    dados_banco = Mecanico.objects.all()
    if request.method == 'POST':
        if 'cancelar' in request.POST:
            return redirect('usuarios:home')
        else:
            nova_equipe = Equipe()
            nova_equipe.nome = request.POST.get('nome')
            mecanico_id = request.POST.get('mecanico')
            mecanico = Mecanico.objects.get(idmecanico=mecanico_id)
            nova_equipe.mecanico = mecanico
            nova_equipe.save()
            return redirect('usuarios:home')
    return render(request, 'cadastro_equipe.html', {'dados_do_banco': dados_banco})
