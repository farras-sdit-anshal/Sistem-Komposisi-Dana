# Generated by Django 3.2.9 on 2021-11-25 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SistemInformasiKeuangan', '0002_sourceoffunds_bank_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account3632',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='account3633',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='account3635',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='account3639',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='account38105',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]