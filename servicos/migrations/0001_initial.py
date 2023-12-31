# Generated by Django 4.2.7 on 2023-12-03 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('mecanicos', '0003_alter_equipe_mecanico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.IntegerField()),
            ],
            options={
                'db_table': 'servico',
            },
        ),
        migrations.CreateModel(
            name='OrdemDeServico',
            fields=[
                ('idordem_de_servico', models.AutoField(primary_key=True, serialize=False)),
                ('data_recebida', models.DateField()),
                ('data_entrega', models.DateField()),
                ('titulo', models.CharField(max_length=150)),
                ('equipe', models.ForeignKey(db_column='idequipe', on_delete=django.db.models.deletion.CASCADE, to='mecanicos.equipe')),
                ('veiculo', models.ForeignKey(db_column='idveiculo', on_delete=django.db.models.deletion.CASCADE, to='clientes.veiculo')),
            ],
            options={
                'db_table': 'ordem_de_servico',
            },
        ),
    ]
