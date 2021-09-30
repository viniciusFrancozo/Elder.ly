from django import forms
from django.forms import ModelForm
from .models import Account
from django.contrib.auth.forms import UserCreationForm
from .models import Voluntario, Idoso


class UsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

class VoluntarioForm(ModelForm):
    class Meta:
        model = Voluntario
        fields = ('agenda', 'disponivel')


class IdosoForm(ModelForm):
    class Meta:
        model = Idoso
        fields = ('em_atendimento',)


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50, required=True)
    senha = forms.PasswordInput()

