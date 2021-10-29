from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from servicos.models import ServicoSolicitado
from cadastro.models import Account, Idoso, Voluntario
# Create your views here.


def listar_servicos(request):
    context = {'servicos': ''}
    servicos = ServicoSolicitado.objects.filter(voluntario_id=None)

    context['servicos'] = servicos
    return render(request, 'listar_servicos.html', context)


def visualizar(request, servico_id):
    servico = get_object_or_404(ServicoSolicitado, pk=servico_id)
    idoso = Account.objects.filter(email=servico.idoso_id)[0]
    context = {
        'servico': servico,
        'user': idoso
    }

    if request.method == 'POST':
        voluntario = Voluntario.objects.get(pk=request.user.voluntario.id)
        servico.voluntario_id = voluntario
        servico.save(update_fields=['voluntario_id'])
        return redirect('index')

    return render(request, 'visualizar.html', context)
