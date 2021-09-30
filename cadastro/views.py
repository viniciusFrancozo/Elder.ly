from django.shortcuts import render, redirect
from .forms import VoluntarioForm, UsuarioForm, IdosoForm
from django.contrib.auth.forms import AuthenticationForm, authenticate
from django.contrib.auth import login
from django.http import Http404


# Create your views here.


def index(request):
    return render(request, 'index.html')


def entrar(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        print(form.error_messages)
        print('passoooooooooooooooou')
        if form.is_valid():
            user = authenticate(request, username=form.username, password=form.password)
            print('passoooooooooooooooou')
            if user is not None:
                print('passoooooooooooooooou')
                login(request, user)
                return redirect('index')

    else:
        form = AuthenticationForm()
    return render(request, 'entrar.html', {'form':form})


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
            return redirect('index')

    else:
        user_form = UsuarioForm(request.POST)
        form = IdosoForm(request.POST)

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
            return redirect('index')

    else:
        user_form = UsuarioForm(request.POST)
        form = VoluntarioForm(request.POST)

    context = {'user_form':user_form, 'form': form}
    return render(request, 'voluntario_cadastro.html', context)

