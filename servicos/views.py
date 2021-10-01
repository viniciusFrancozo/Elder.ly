from django.shortcuts import render
from .forms import ServicoModel
from cadastro.models import Idoso

# Create your views here.

def solicitar_servico(request):
    user = request.user
    if request.method == 'POST':
        form = ServicoModel(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.idoso_id = Idoso.objects.filter(idoso_id=user.id)[0]
            new_form.save()
    else:
        form = ServicoModel()

    return render(request, 'solicitar_servico.html', {'form': form})

