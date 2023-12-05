from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import OrdemDeServico
from clientes.models import Veiculo
from mecanicos.models import Equipe
def cadastro_ordem(request):
    veiculos_banco = Veiculo.objects.all()
    equipes_banco = Equipe.objects.all()

    if request.method == 'POST':
        if 'cancelar' in request.POST:
            return redirect('usuarios:home')
        else:
            nova_ordem = OrdemDeServico()
            nova_ordem.titulo = request.POST.get('titulo')
            nova_ordem.data_recebida = request.POST.get('data_recebida')
            nova_ordem.data_entrega = request.POST.get('data_entrega')

            veiculo_id = request.POST.get('veiculo')
            veiculo = Veiculo.objects.get(idveiculo = veiculo_id)
            nova_ordem.veiculo = veiculo

            equipe_id = request.POST.get('equipe')
            equipe = Equipe.objects.get(idequipe = equipe_id)
            nova_ordem.equipe = equipe

            

            nova_ordem.save()
            return redirect('usuarios:home')
    return render(request, 'ordem.html', {'veiculos_do_banco': veiculos_banco, 'equipes_do_banco': equipes_banco} )



