from django.shortcuts import render
from helpfunctions.index import userRole
from .forms import PerfilIdoso, PerfilGeral, PerfilVoluntario
# Create your views here.


def perfil(request):
    user = request.user
    context = userRole(user)
    print(context)
    if request.method == 'POST':
        form_user = PerfilGeral(request.POST)
        if context['role'] == 'I':
            form = PerfilIdoso(request.POST)
        elif context['role'] == 'V':
            form = PerfilVoluntario(request.POST)
        else:
            form = ''
            form_user = ''
        if form.is_valid():
            form.save()
    else:
        form_user = PerfilGeral()
        if context['role'] == 'I':
            print('teste')
            form = PerfilIdoso()
        elif context['role'] == 'V':
            form = PerfilVoluntario()
        else:
            form = ''
            form_user = ''

    context['form'] = form
    context['form_user'] = form_user
    print(context)
    return render(request, 'perfil.html', context)