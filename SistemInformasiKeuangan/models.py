from django.db import models


# Create your models here.
class SourceOfFunds(models.Model):
    description = models.CharField(max_length=100, help_text="")
    kode = models.CharField(max_length=15, help_text="")
    bank_account = models.CharField(max_length=20, help_text="", default="")

    class Meta:
        ordering = ['kode']


class VaType(models.Model):
    va_name = models.CharField(max_length=50, help_text="VA's name")
    va_id = models.CharField(max_length=30, help_text="VA Id's number")
    code = models.OneToOneField(SourceOfFunds, on_delete=models.PROTECT)


class Transactions(models.Model):
    reference_number = models.CharField(max_length=100, help_text="")
    transaction_date = models.DateField(help_text="")
    effective_date = models.DateField(help_text="")
    debit = models.IntegerField()
    credit = models.IntegerField()
    balance = models.IntegerField()
    description = models.IntegerField()
    code_sof = models.ForeignKey(VaType, models.PROTECT)

    class Meta:
        abstract = True


class Account38105(Transactions):
    def __str__(self):
        return self


class Account3632(Transactions):
    def __str__(self):
        return self


class Account3633(Transactions):
    def __str__(self):
        return self


class Account3635(Transactions):
    def __str__(self):
        return self


class Account3639(Transactions):
    def __str__(self):
        return self


# ----------------------------------------------------------------------------
# Documentation
# ----------------------------------------------------------------------------
# --- One to One filed ---
# https://docs.djangoproject.com/en/3.2/topics/db/examples/one_to_one/
#
# --- Summary if, trough django orm ---
# https://stackoverflow.com/questions/36573640/how-to-sum-only-positive-values-with-django-conditional-aggregates
#
# --- Model inheritance
# https://docs.djangoproject.com/en/3.2/topics/db/models/#abstract-base-classes
#
# https://docs.djangoproject.com/en/3.2/ref/models/conditional-expressions/
