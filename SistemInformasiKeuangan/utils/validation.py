def validation_transaction(save_path, csv, xlrd, obj_bank_account):
    list_validation_value = []
    try:
        last_transaction = obj_bank_account.objects.order_by('id').last().balance
    except:
        last_transaction = 0

    print(last_transaction)
    with open(save_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for data in csv_reader:
            # convert date excel ke object date python
            data['Tgl Transaksi'] = xlrd.xldate_as_datetime(int(data['Tgl Transaksi']), 0)
            data['Tgl Efektif'] = xlrd.xldate_as_datetime(int(data['Tgl Efektif']), 0)

            # convert string to int
            data['Debit'] = 0 if data['Debit'] == "" else int(data['Debit'])
            data['Kredit'] = 0 if data['Kredit'] == "" else int(data['Kredit'])
            data['Saldo'] = 0 if data['Saldo'] == "" else int(data['Saldo'])

            # check whether transaction is valid or not
            last_transaction += data["Kredit"] - data["Debit"]
            if last_transaction == data["Saldo"]:
                list_validation_value.append(True)
            else:
                # print(last_transaction)
                list_validation_value.append(False)

    return not False in list_validation_value
