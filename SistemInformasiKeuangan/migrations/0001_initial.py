# Generated by Django 3.2.9 on 2021-11-24 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SourceOfFunds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('kode', models.CharField(max_length=15)),
            ],
            options={
                'ordering': ['kode'],
            },
        ),
        migrations.CreateModel(
            name='VaType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('va_name', models.CharField(help_text="VA's name", max_length=50)),
                ('va_id', models.CharField(help_text="VA Id's number", max_length=30)),
                ('code', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='SistemInformasiKeuangan.sourceoffunds')),
            ],
        ),
        migrations.CreateModel(
            name='Account38105',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(max_length=100)),
                ('transaction_date', models.DateField()),
                ('effective_date', models.DateField()),
                ('debit', models.IntegerField()),
                ('credit', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('description', models.IntegerField()),
                ('code_sof', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='SistemInformasiKeuangan.vatype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Account3639',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(max_length=100)),
                ('transaction_date', models.DateField()),
                ('effective_date', models.DateField()),
                ('debit', models.IntegerField()),
                ('credit', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('description', models.IntegerField()),
                ('code_sof', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='SistemInformasiKeuangan.vatype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Account3635',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(max_length=100)),
                ('transaction_date', models.DateField()),
                ('effective_date', models.DateField()),
                ('debit', models.IntegerField()),
                ('credit', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('description', models.IntegerField()),
                ('code_sof', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='SistemInformasiKeuangan.vatype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Account3633',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(max_length=100)),
                ('transaction_date', models.DateField()),
                ('effective_date', models.DateField()),
                ('debit', models.IntegerField()),
                ('credit', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('description', models.IntegerField()),
                ('code_sof', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='SistemInformasiKeuangan.vatype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Account3632',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(max_length=100)),
                ('transaction_date', models.DateField()),
                ('effective_date', models.DateField()),
                ('debit', models.IntegerField()),
                ('credit', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('description', models.IntegerField()),
                ('code_sof', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='SistemInformasiKeuangan.vatype')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
