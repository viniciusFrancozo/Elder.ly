from django.shortcuts import render


# Create your views here.

def solicitar_servico(request):
    render(request, 'solicitar_servico.html')