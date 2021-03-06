# Generated by Django 3.2.7 on 2021-10-01 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0007_auto_20211001_1802'),
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicoSolicitado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servsolicitado', models.CharField(max_length=30, verbose_name='Serviço')),
                ('tagservico', models.CharField(choices=[('1', 'Serviços da Casa'), ('2', 'Acompanhamento / Carona'), ('3', 'Compras'), ('4', 'Visita'), ('5', 'Diversos')], max_length=15, verbose_name='Etiqueta')),
                ('data_compromisso', models.DateField(verbose_name='Data')),
                ('hora_compromisso', models.TimeField(verbose_name='Horário')),
                ('data_inicio', models.DateField(blank=True, null=True)),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('hora_inicio', models.TimeField(blank=True, null=True)),
                ('hora_fim', models.TimeField(blank=True, null=True)),
                ('observacao', models.TextField(blank=True, verbose_name='Observação')),
                ('idoso_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='cadastro.idoso')),
                ('voluntario_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='cadastro.voluntario')),
            ],
        ),
        migrations.DeleteModel(
            name='Servico',
        ),
    ]
