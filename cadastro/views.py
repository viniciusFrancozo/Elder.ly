from django.shortcuts import render, redirect
from .forms import VoluntarioForm, UsuarioForm, IdosoForm
from django.contrib.auth import login
from .models import Voluntario, Idoso


# Create your views here.


def index(request):
    user = request.user

    if not Voluntario.objects.filter(voluntario_id=user.id):
        if not Idoso.objects.filter(idoso_id=user.id):
            context = {
                'user': user,
                'qs': [],
                'role': 'adm'
            }
        else:
            qs = Idoso.objects.filter(idoso_id=user.id)
            context = {
                'user': user,
                'qs': qs,
                'role': 'I'
            }
    else:
        qs = Voluntario.objects.filter(voluntario_id=user.id)
        context = {
            'user': user,
            'qs': qs,
            'role': 'V'
        }

    return render(request, 'index.html', context)



def pag_cadastro(request):
    return render(request, 'cadastro.html')


def elder_cadastro(request):
    if request.method == 'POST':
        user_form = UsuarioForm(request.POST)
        form = IdosoForm(request.POST)

        if user_form.is_valid() and form.is_valid():
            user = user_form.save()

            idoso = form.save(commit=False)
            idoso.idoso = user

            idoso.save()

            login(request, user)
            return redirect('index')

    else:
        user_form = UsuarioForm()
        form = IdosoForm()

    context = {'user_form': user_form, 'form': form}
    return render(request, 'elder_cadastro.html', context)


def voluntario_cadastro(request):
    if request.method == 'POST':
        user_form = UsuarioForm(request.POST)
        form = VoluntarioForm(request.POST)

        if user_form.is_valid() and form.is_valid():
            user = user_form.save()

            voluntario = form.save(commit=False)
            voluntario.voluntario = user

            voluntario.save()

            login(request, user)
            return redirect('index')

    else:
        user_form = UsuarioForm()
        form = VoluntarioForm()

    context = {'user_form':user_form, 'form': form}
    return render(request, 'voluntario_cadastro.html', context)


def perfil_voluntario(request):
    pass


def perfil_idoso(request):
    pass
