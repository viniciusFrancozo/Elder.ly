from django.shortcuts import render


# Create your views here.

def solicitar_servico(request):
    return render(request, 'solicitar_servico.html')

