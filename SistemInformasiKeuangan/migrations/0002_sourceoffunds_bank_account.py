# Generated by Django 3.2.9 on 2021-11-24 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SistemInformasiKeuangan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourceoffunds',
            name='bank_account',
            field=models.CharField(default='', max_length=20),
        ),
    ]
