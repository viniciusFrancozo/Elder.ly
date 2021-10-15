from django import forms
from cadastro.models import Idoso, Voluntario, Account

class PerfilGeral(forms.ModelForm):
    class Meta:
        model = Account
        labels = {
            'first_name': '',
            'last_name': '',
            'estado': '',
            'cidade': '',
            'cep': '',
            'bairro': '',
            'rua': '',
            'numero_res': '',
            'rg': '',
            'cpf': '',
            'telefone': '',
            'estado_civil': '',
            'sexo': '',
            'escolaridade': '',

        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Sobrenome'}),
            'estado': forms.TextInput(attrs={'placeholder': 'Estado'}),
            'cidade': forms.TextInput(attrs={'placeholder': 'Cidade'}),
            'cep': forms.TextInput(attrs={'placeholder': 'CEP'}),
            'bairro': forms.TextInput(attrs={'placeholder': 'Bairro'}),
            'rua': forms.TextInput(attrs={'placeholder': 'Rua'}),
            'numero_res': forms.TextInput(attrs={'placeholder': 'Número'}),
            'rg': forms.TextInput(attrs={'placeholder': 'RG'}),
            'cpf': forms.TextInput(attrs={'placeholder': 'CPF'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Telefone'}),
            'escolaridade': forms.TextInput(attrs={'placeholder': 'Escolaridade'}),
        }

        exclude = ('email','password', 'username', 'date_joined', 'last_login', 'is_admin', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')

class PerfilIdoso(forms.ModelForm):
    class Meta:
        model = Idoso
        exclude = ('idoso', 'em_atendimento')

class PerfilVoluntario(forms.ModelForm):
    class Meta:
        model = Voluntario
        labels = {
            'agenda': ''
        }
        exclude = ('voluntario', 'disponivel')