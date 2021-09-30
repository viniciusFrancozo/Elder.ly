from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver


class MyAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('O usuário deve conter um e-mail válido')

        user = self.model(
            email=self.normalize_email(email),
            first_name=self.first_name,
            last_name=self.last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError('O usuário deve conter um e-mail válido')

        user = self.create_user(
            email=self.normalize_email(email),
            password = password
        )

        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True

        user.save(using=self._db)
        return user


class Account(AbstractUser, PermissionsMixin):
    """ New user model for attending elderly demands """

    # Account registration data
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30)

    # Data required for serving or request a service
    estado = models.CharField(max_length=30, blank=True)
    cidade = models.CharField(max_length=50, blank=True)
    cep = models.CharField(verbose_name='CPF', max_length=10, blank=True)
    bairro = models.CharField(max_length=50, blank=True)
    rua = models.CharField(max_length=50, blank=True)
    numero_res = models.CharField(verbose_name='Número', max_length=6, blank=True)
    first_name = models.CharField(verbose_name='Nome', max_length=50)
    last_name = models.CharField(verbose_name='Sobrenome', max_length=50)
    rg = models.CharField(verbose_name='RG',max_length=50, blank=True)
    cpf = models.CharField(verbose_name='CPF',max_length=50, blank=True)
    telefone = models.CharField(max_length=50, blank=True)
    estado_civil = models.CharField(max_length=10,
        choices=(
            ('CASADO', 'Casado(a)'),
            ('SOLTEIRO', 'Solteiro(a)'),
            ('DIVORCIADO', 'Divorciado(a)'),
            ('VIUVO', 'Viúvo(a)'),
            ('OUTROS', 'Outros')
        ), default='OUTROS'
    )
    escolaridade = models.CharField(max_length=30, blank=True)
    sexo = models.CharField(max_length=10,
        choices=(
            ('MASCULINO', 'Masculino'),
            ('FEMININO', 'Feminino')
        ), default='MASCULINO'
    )

    # Required Django AbstractUser model fields
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Voluntario(models.Model):
    # one-to-one link with the Account model (used to create a "profile" for the Account model)
    voluntario = models.OneToOneField(Account, on_delete=models.CASCADE)

    # Voluntario data for serving
    agenda = models.CharField(max_length=10,
        choices=(
            ('MANHA', 'Manhã'),
            ('TARDE', 'Tarde'),
            ('NOITE', 'Noite'),
            ('ANY', 'Qualquer Horário')
        ), default='ANY'
    )
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.voluntario.email


class Idoso(models.Model):
    # one-to-one link with the Account model (used to create a "profile" for the Account model)
    idoso = models.OneToOneField(Account, on_delete=models.CASCADE)

    # Voluntario data for serving
    em_atendimento = models.BooleanField(default=False)

    def __str__(self):
        return self.idoso.email