from django.forms import ModelForm
from cadastro.models import Idoso, Voluntario, Account

class PerfilGeral(ModelForm):
    class Meta:
        model = Account
        exclude = ('password', 'username', 'date_joined', 'last_login', 'is_admin', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')

class PerfilIdoso(ModelForm):
    class Meta:
        model = Idoso
        exclude = ('idoso', 'em_atendimento')

class PerfilVoluntario(ModelForm):
    class Meta:
        model = Voluntario
        fields = '__all__'