# Generated by Django 4.2.7 on 2023-12-02 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mecanicos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='mecanico',
            table='mecanico',
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('mecanico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mecanicos.mecanico')),
            ],
            options={
                'db_table': 'equipe',
            },
        ),
    ]
