# Generated by Django 2.0 on 2019-12-12 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='ФИО')),
                ('specialization', models.CharField(max_length=300, verbose_name='Специализация')),
                ('info', models.CharField(max_length=10000, verbose_name='Инфо о враче')),
            ],
            options={
                'verbose_name': 'Врач',
                'verbose_name_plural': 'Врачи',
            },
        ),
        migrations.CreateModel(
            name='Reception',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата приема ')),
                ('date_delete', models.DateField(verbose_name='Время удаления')),
                ('time', models.CharField(max_length=5, verbose_name='Время приема ')),
                ('patient_name', models.CharField(max_length=300, verbose_name='ФИО ')),
                ('patient_info', models.CharField(max_length=10000, verbose_name='Инфо о пациенте ')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Doctor', verbose_name='Доктор ')),
            ],
            options={
                'verbose_name': 'Прием',
                'verbose_name_plural': 'Приемы',
            },
        ),
    ]