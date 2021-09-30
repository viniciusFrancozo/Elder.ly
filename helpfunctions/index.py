from cadastro.models import Voluntario, Idoso


def userRole(user):
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
    return context