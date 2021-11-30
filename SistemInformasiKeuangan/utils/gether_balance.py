from django.db.models import Sum, Q


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
    id_sof_3632 = SourceOfFunds.objects.filter(Q(bank_account=bank_account_str), Q(kode__contains=division_str)).all()
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
