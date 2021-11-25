from django.shortcuts import render, redirect, get_object_or_404
from .forms import ServicoModel
from cadastro.models import Idoso, Account, Voluntario
from .models import ServicoSolicitado
import datetime

# Create your views here.


def solicitar_servico(request):
    user = request.user
    if request.method == 'POST':
        form = ServicoModel(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.idoso_id = Idoso.objects.filter(idoso_id=user.id)[0]
            new_form.save()
            return redirect('index')
    else:
        form = ServicoModel()

    return render(request, 'solicitar_servico.html', {'form': form})


def meus_servicos(request):
    idoso = request.user.idoso

    abertos = ServicoSolicitado.objects.filter(idoso_id=idoso.id, voluntario_id__isnull=True)
    aguardando = ServicoSolicitado.objects.filter(idoso_id=idoso.id).exclude(voluntario_id__isnull=True).exclude(confirmado=True)
    em_andamento = ServicoSolicitado.objects.filter(idoso_id=idoso.id).exclude(confirmado=False).exclude(data_fim__isnull=False)
    concluidos = ServicoSolicitado.objects.filter(idoso_id=idoso.id).exclude(data_fim__isnull=True).exclude(data_inicio__isnull=True)

    context = {
        'abertos': abertos,
        'aguardando': {},
        'em_andamento': em_andamento,
        'concluidos': concluidos
    }

    for i in aguardando:
        v = Voluntario.objects.get(id=i.voluntario_id_id)
        context['aguardando'][i] = Account.objects.get(id=v.voluntario_id)

    return render(request, 'meus_servicos.html', context)

def meus_servicos_voluntario(request):
    voluntario = request.user.voluntario

    aguardando = ServicoSolicitado.objects.filter(voluntario_id=voluntario.id).exclude(confirmado=True)
    em_andamento = ServicoSolicitado.objects.filter(voluntario_id=voluntario.id).exclude(confirmado=False).exclude(data_fim__isnull=False)
    concluidos = ServicoSolicitado.objects.filter(voluntario_id=voluntario.id).exclude(data_fim__isnull=True).exclude(data_inicio__isnull=True)

    context = {
        'aguardando': {},
        'em_andamento': em_andamento,
        'concluidos': concluidos
    }

    for i in aguardando:
        v = Idoso.objects.get(id=i.idoso_id_id)
        context['aguardando'][i] = Account.objects.get(id=v.idoso_id)

    return render(request, 'meus_servicos_voluntario.html', context)

def confirmar(request, servico_id):
    servico = get_object_or_404(ServicoSolicitado, pk=servico_id)
    idoso = Account.objects.filter(email=servico.idoso_id)[0]
    voluntario_fields = Account.objects.filter(email=servico.voluntario_id)[0]
    context = {
        'servico': servico,
        'user': idoso,
        'voluntario': voluntario_fields
    }

    if request.method == 'POST':
        servico.confirmado = True
        servico.save(update_fields=['confirmado'])
        return redirect('index')

    return render(request, 'confirmar.html', context)


def iniciar(request, servico_id):
    servico = get_object_or_404(ServicoSolicitado, pk=servico_id)
    v = Idoso.objects.get(id=servico.idoso_id_id)
    context = {
        'idoso': Account.objects.get(id=v.idoso_id),
        'servico': servico
    }
    print(context['idoso'])

    if request.method == 'POST':
        servico.data_inicio = datetime.datetime.today()
        servico.hora_inicio = datetime.datetime.now().strftime("%H:%M:%S")
        servico.save(update_fields=['data_inicio', 'hora_inicio'])
        return redirect('index')

    return render(request, 'iniciar.html', context)


def encerrar(request, servico_id):
    servico = get_object_or_404(ServicoSolicitado, pk=servico_id)
    context = {
        "servico": servico
    }
    if request.method == 'POST':
        servico.data_fim = datetime.datetime.today()
        servico.hora_fim = datetime.datetime.now().strftime("%H:%M:%S")
        servico.save(update_fields=['data_fim', 'hora_fim'])
        return redirect('index')

    return render(request, 'encerrar.html', context)
