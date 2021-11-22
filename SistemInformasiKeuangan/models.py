from django.db import models


# Create your models here.
class VaType(models.Model):
    va_name = models.CharField(max_length=50, help_text="VA's name")
    va_id = models.CharField(max_length=30, help_text="VA Id's number")


class Transactions(models.Model):
    reference_number = models.CharField(max_length=100, help_text="")
    transaction_date = models.DateField(help_text="")
    effective_date = models.DateField(help_text="")
    debit = models.IntegerField()
    credit = models.IntegerField()
    balance = models.IntegerField()
    description = models.IntegerField()
    va_type = models.ForeignKey(VaType, models.PROTECT)

