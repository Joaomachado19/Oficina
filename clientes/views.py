from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Cliente,Veiculo

def cadastro_cliente(request):
    if request.method == 'POST':
        if 'cancelar' in request.POST:
            return redirect('usuarios:home')
        else:
          
            novo_cliente = Cliente()
            novo_cliente.nome = request.POST.get('nome')
            novo_cliente.telefone = request.POST.get('telefone')
            novo_cliente.endereco = request.POST.get('endereco')
            novo_cliente.save()


            novo_veiculo = Veiculo()
            novo_veiculo.placa = request.POST.get('placa')
            novo_veiculo.modelo = request.POST.get('modelo')
            novo_veiculo.ano = request.POST.get('ano')
            novo_veiculo.defeito = request.POST.get('defeito')
            novo_veiculo.cliente = novo_cliente 
            novo_veiculo.save()

            return redirect('usuarios:home')

    return render(request, 'cadastro_cliente.html')
