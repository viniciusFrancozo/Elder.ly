# Generated by Django 3.2.7 on 2021-09-28 23:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_alter_account_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idoso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('em_atendimento', models.BooleanField(default=False)),
                ('idoso', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
