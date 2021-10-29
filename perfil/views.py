from django.shortcuts import render
from helpfunctions.index import userRole
from .forms import PerfilIdoso, PerfilGeral, PerfilVoluntario
# Create your views here.


def perfil(request):
    user = request.user
    context = userRole(user)
    if request.method == 'POST':
        form_user = PerfilGeral(request.POST, instance=user)
        if context['role'] == 'I':
            form = PerfilIdoso(request.POST, instance=user.idoso)
        elif context['role'] == 'V':
            form = PerfilVoluntario(request.POST, instance=user.voluntario)
        else:
            form = ''
            form_user = ''
        if form.is_valid() and form_user.is_valid():
            if context['role'] == 'I':
                user = form_user.save()
                midd = form.save(commit=False)
                midd.voluntario = user
                midd.save()
            else:
                form_user.save()
                form.save()
    else:
        form_user = PerfilGeral(instance=user)
        if context['role'] == 'I':
            form = PerfilIdoso(instance=user.idoso)
        elif context['role'] == 'V':
            form = PerfilVoluntario(instance=user.voluntario)
        else:
            form = ''
            form_user = ''

    context['form'] = form
    context['form_user'] = form_user
    return render(request, 'perfil.html', context)