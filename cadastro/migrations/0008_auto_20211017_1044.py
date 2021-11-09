# Generated by Django 3.2.7 on 2021-10-17 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0007_auto_20211001_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='estado_civil',
            field=models.CharField(choices=[('', 'Estado Civíl'), ('CASADO', 'Casado(a)'), ('SOLTEIRO', 'Solteiro(a)'), ('DIVORCIADO', 'Divorciado(a)'), ('VIUVO', 'Viúvo(a)'), ('OUTROS', 'Outros')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=150, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(max_length=150, verbose_name='Sobrenome'),
        ),
        migrations.AlterField(
            model_name='account',
            name='sexo',
            field=models.CharField(choices=[('', 'Sexo'), ('MASCULINO', 'Masculino'), ('FEMININO', 'Feminino')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='voluntario',
            name='agenda',
            field=models.CharField(choices=[('', 'Seu Horário Preferido'), ('MANHA', 'Manhã'), ('TARDE', 'Tarde'), ('NOITE', 'Noite'), ('ANY', 'Qualquer Horário')], default='', max_length=10),
        ),
    ]