from django.shortcuts import render
from .forms import ServicoModel

# Create your views here.

def solicitar_servico(request):
    user = request.user
    if request.method == 'POST':
        form = ServicoModel(request.POST)
        if form.is_valid():
            print(form)
            form.save()
    else:
        form = ServicoModel()

    return render(request, 'solicitar_servico.html',{'form':form})

