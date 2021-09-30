from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, Voluntario, Idoso


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username')
    search_fields = ('email',)
    fieldsets = (
        (None, {'fields': (
            'email',
            'password',
            'username',
            'estado',
            'cidade',
            'cep',
            'bairro',
            'rua',
            'numero_res',
            'primeiro_nome',
            'sobrenome',
            'rg',
            'cpf',
            'telefone',
            'estado_civil',
            'escolaridade',
            'sexo',
        )}),
        ('Permissions', {'fields': ('is_admin','is_staff','is_superuser','is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    filter_horizontal = ()
    filter_vertical = ()



admin.site.register(Account, AccountAdmin)
admin.site.register(Voluntario)
admin.site.register(Idoso)