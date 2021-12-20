import time

from django.db.models import Sum, Q, Min, Max
from datetime import timedelta, timezone


def balance_of_account(SourceOfFunds, bank_account_str, obj_bank_accunt, obj_bank_addjustment):
    result_sum_data = {}
    id_sof_3632 = SourceOfFunds.objects.filter(Q(bank_account=bank_account_str)).all()
    for data in id_sof_3632:
        # print(data.id)
        # Credit and debit on account 3632
        credit = obj_bank_accunt.objects.filter(code_sof=data.id).aggregate(Sum('credit'))["credit__sum"]
        debit = obj_bank_accunt.objects.filter(code_sof=data.id).aggregate(Sum('debit'))["debit__sum"]

        # credit and debit on account adjustment
        credit_adjustment = obj_bank_addjustment.objects.filter(code_sof=data.id).aggregate(Sum('credit'))[
            "credit__sum"]
        debit_adjustment = obj_bank_addjustment.objects.filter(code_sof=data.id).aggregate(Sum('debit'))["debit__sum"]

        val_credit = 0 if credit is None else credit
        val_debit = 0 if debit is None else debit
        val_credit_adjustment = 0 if credit_adjustment is None else credit_adjustment
        val_debit_adjustment = 0 if debit_adjustment is None else debit_adjustment
        balance = (val_credit - val_debit) + (val_credit_adjustment - val_debit_adjustment)

        result_sum_data[data.description] = balance

    return result_sum_data


def balance_of_account_38105(SourceOfFunds, bank_account_str, division_str, obj_bank_accunt, obj_bank_addjustment):
    result_sum_data = {}
    id_sof_3632 = SourceOfFunds.objects.filter(Q(bank_account=bank_account_str), Q(kode__endswith=division_str)).all()
    for data in id_sof_3632:
        # print(data.id)
        # Credit and debit on account 3632
        credit = obj_bank_accunt.objects.filter(code_sof=data.id).aggregate(Sum('credit'))["credit__sum"]
        debit = obj_bank_accunt.objects.filter(code_sof=data.id).aggregate(Sum('debit'))["debit__sum"]

        # credit and debit on account adjustment
        credit_adjustment = obj_bank_addjustment.objects.filter(code_sof=data.id).aggregate(Sum('credit'))[
            "credit__sum"]
        debit_adjustment = obj_bank_addjustment.objects.filter(code_sof=data.id).aggregate(Sum('debit'))["debit__sum"]

        val_credit = 0 if credit is None else credit
        val_debit = 0 if debit is None else debit
        val_credit_adjustment = 0 if credit_adjustment is None else credit_adjustment
        val_debit_adjustment = 0 if debit_adjustment is None else debit_adjustment
        balance = (val_credit - val_debit) + (val_credit_adjustment - val_debit_adjustment)

        result_sum_data[data.description] = balance
        # print(result_sum_data)

    return result_sum_data


def sum_if_date(obj_bank_accunt):
    result_sum_if_date = {}

    # take the first date on Account
    latest_date = obj_bank_accunt.objects.all().aggregate(Min('transaction_date'))["transaction_date__min"]
    newest_date = obj_bank_accunt.objects.all().aggregate(Max('transaction_date'))["transaction_date__max"]
    running_date = latest_date

    # If databse is null its shoud give an error cause "<=" not superted on instance NoneType
    # So i have to check is newest data and running date is NoneType or Not

    if newest_date is not None:

        while running_date <= newest_date:
            balance = \
                obj_bank_accunt.objects.filter(transaction_date__range=[latest_date, running_date]).aggregate(
                    Sum('credit'))[
                    "credit__sum"] - \
                obj_bank_accunt.objects.filter(transaction_date__range=[latest_date, running_date]).aggregate(Sum('debit'))[
                    "debit__sum"]
            # print( "{} sampai dengan {} saldo : {}".format(running_date.strftime("%d %B %Y"), newest_date.strftime(
            # "%d%B %Y"), balance))

            result_sum_if_date[time.mktime(running_date.timetuple())] = balance

            running_date += timedelta(days=1)

    return result_sum_if_date
