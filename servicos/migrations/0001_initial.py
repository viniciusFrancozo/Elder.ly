# Generated by Django 3.2.7 on 2021-09-30 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastro', '0005_idoso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servsolicitado', models.CharField(max_length=30)),
                ('data_inicio', models.DateField(blank=True, null=True)),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('hora_inicio', models.TimeField(blank=True, null=True)),
                ('hora_fim', models.TimeField(blank=True, null=True)),
                ('observacao', models.TextField(blank=True)),
                ('idoso_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='cadastro.idoso')),
                ('voluntario_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='cadastro.voluntario')),
            ],
        ),
    ]
