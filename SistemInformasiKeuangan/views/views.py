import datetime
import json
import os
import mimetypes
import csv
import re
import xlrd
import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from os.path import exists
from SistemInformasiKeuangan.models import *
from SistemInformasiKeuangan.utils import validation, gether_balance, gv_api

# Create your views here.
from django.conf import settings

# enable iframe
from django.views.decorators.clickjacking import xframe_options_exempt


def home(request):
    return render(request, "index.html")


def dashboard(request):
    return render(request, "dashboard/dist/index.html")


def login(request):
    return render(request, "dashboard/dist/login.html")


def index(request):
    user = request.user
    if user.is_authenticated:
        return redirect(dashboard)
    else:
        return render(request, 'index.html')


def inputData(request):
    # check wehter is file uploaded or not

    user = request.user
    if user.is_authenticated:
        if validation.validation_groups(user, "Accountant"):
            return render(request, "dashboard/dist/input.html")
        else:
            demanded_access = "Komposisi Dana"
            return render(request, "dashboard/dist/401.html", {'userData': user, 'demand_access': demanded_access})

    else:
        return render(request, 'index.html')


def processform(request):
    save_path = ""

    is_uploaded = request.FILES.get('file-mutasi', False)
    bank_account = request.POST.get('bank-account', False)
    account_banks = {"1210038105": Account38105, "1220003632": Account3632, "1220003633": Account3633,
                     "1220003635": Account3635, "1210103639": Account3639, "adjustment": AccountAdjustment}
    source_of_funds_text = "sumber dana"
    # print(bank_account)

    if is_uploaded and bank_account and (bank_account in account_banks.keys()):

        obj_bank_account = account_banks[bank_account]

        if request.method == 'POST':
            save_path = os.path.join(settings.MEDIA_ROOT, request.FILES["file-mutasi"].name)
            with open(save_path, "wb") as output_file:
                for chunk in request.FILES["file-mutasi"].chunks():
                    output_file.write(chunk)

        # is file exist
        if exists(save_path):

            for typeFile in mimetypes.guess_type(save_path):
                # print(mimetypes.guess_extension(typeFile))
                if typeFile is not None:

                    posible_extension = (mimetypes.guess_all_extensions(typeFile))
                    if ".csv" in posible_extension:

                        # Kekacauan hakiki, ditinggal 1 minggu lupa semua
                        is_adjustment = obj_bank_account == AccountAdjustment

                        is_valid = validation.validation_transaction(save_path, csv, xlrd, obj_bank_account) if is_adjustment is False else True
                        if is_valid:

                            # read csv
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

                                    # Check whether CSV file containse sof or not, if yes input sofId directly to DB
                                    if source_of_funds_text in data.keys():

                                        # Import to db
                                        id_sof = SourceOfFunds.objects.get(kode=data["sumber dana"]).id
                                        # print(id_sof)
                                        obj_bank_account.objects.create(reference_number=data["Nomor Referensi"],
                                                                        transaction_date=data["Tgl Transaksi"],
                                                                        effective_date=data["Tgl Efektif"],
                                                                        debit=data["Debit"],
                                                                        credit=data["Kredit"],
                                                                        balance=data["Saldo"],
                                                                        description=data["Keterangan"],
                                                                        code_sof_id=id_sof)

                                    else:

                                        # If csv file not contain sofId then lets python create code that
                                        # separate va transactions and non va transaction

                                        # Variable that contain keterangan (descriptions of transaction)
                                        transaction_description = data["Keterangan"]

                                        is_va = re.search("VA : 8166", transaction_description)
                                        if is_va is not None:
                                            # Va transaction
                                            va_code = transaction_description[is_va.start() + 9: is_va.start() + 11]

                                            # get from model to determine sof forms va code
                                            va_type_object_id = VaType.objects.get(va_id=va_code).code_id

                                            # Get from model code_sof_id BTT (Belum Tercatat)



                                            code_sof_id_from_va_transaction = SourceOfFunds.objects.get(
                                                id=va_type_object_id).id

                                            # insert object to db
                                            obj_bank_account.objects.create(reference_number=data["Nomor Referensi"],
                                                                            transaction_date=data["Tgl Transaksi"],
                                                                            effective_date=data["Tgl Efektif"],
                                                                            debit=data["Debit"],
                                                                            credit=data["Kredit"],
                                                                            balance=data["Saldo"],
                                                                            description=data["Keterangan"],
                                                                            code_sof_id=code_sof_id_from_va_transaction)

                                        else:
                                            # Transaction non va
                                            # insert object to db with code_sof_id as OTHER
                                            not_record_yet_code_sof_id = SourceOfFunds.objects.get(kode="BTT").id
                                            # insert object to db
                                            obj_bank_account.objects.create(reference_number=data["Nomor Referensi"],
                                                                            transaction_date=data["Tgl Transaksi"],
                                                                            effective_date=data["Tgl Efektif"],
                                                                            debit=data["Debit"],
                                                                            credit=data["Kredit"],
                                                                            balance=data["Saldo"],
                                                                            description=data["Keterangan"],
                                                                            code_sof_id=not_record_yet_code_sof_id)
                        else:
                            # trasanctin not valid
                            print("Transaction isnt valid")

                    else:
                        print("File must be csv")

        return render(request, "dashboard/dist/forms-process.html")
    else:
        return redirect(inputData)


@login_required
@xframe_options_exempt
def dashboard(request):

    user = request.user

    # check wether they have acceses to dashboard or not
    if validation.validation_groups(user, "g_keuangan"):

        auth0user = user.social_auth.get(provider='auth0')
        userdata = {
            'user_id': auth0user.uid,
            'name': user.first_name,
            'picture': auth0user.extra_data['picture'],
            'email': auth0user.extra_data['email'],
        }

        sof_values_3632 = gether_balance.balance_of_account(SourceOfFunds, "1220003632", Account3632, AccountAdjustment)
        sof_values_3633 = gether_balance.balance_of_account(SourceOfFunds, "1220003633", Account3633, AccountAdjustment)
        sof_values_3635 = gether_balance.balance_of_account(SourceOfFunds, "1220003635", Account3635, AccountAdjustment)
        sof_values_3639 = gether_balance.balance_of_account(SourceOfFunds, "1210103639", Account3639, AccountAdjustment)
        sof_values_38105_sdit = gether_balance.balance_of_account_38105(SourceOfFunds, "1210038105", "SDIT",
                                                                        Account38105, AccountAdjustment)
        sof_values_38105_tkit_ae = gether_balance.balance_of_account_38105(SourceOfFunds, "1210038105", "TKIT AE",
                                                                           Account38105, AccountAdjustment)
        sof_values_38105_tkit_ans = gether_balance.balance_of_account_38105(SourceOfFunds, "1210038105", "TKIT ANS",
                                                                            Account38105, AccountAdjustment)

        balance_date_3632 = gether_balance.sum_if_date(Account3632)
        balance_date_3633 = gether_balance.sum_if_date(Account3633)
        balance_date_3635 = gether_balance.sum_if_date(Account3635)
        balance_date_3639 = gether_balance.sum_if_date(Account3639)
        balance_date_38105 = gether_balance.sum_if_date(Account38105)

        # retrieve data from ypiiah.id
        # Gets entries associated with a specific forms.
        gf_json_3632 = gv_api.respone_gv_api()

        # print(gf_json_3632)

        return render(request, 'dashboard/dist/index.html', {
            'auth0User': auth0user,
            'userdata': userdata,
            'data_3632': sof_values_3632,
            'data_3633': sof_values_3633,
            'data_3635': sof_values_3635,
            'data_3639': sof_values_3639,
            'data_38105_sdit': sof_values_38105_sdit,
            'data_38105_tkit_ae': sof_values_38105_tkit_ae,
            'data_38105_tkit_ans': sof_values_38105_tkit_ans,
            'sum_data_3632': sum(sof_values_3632.values()),
            'sum_data_3633': sum(sof_values_3633.values()),
            'sum_data_3635': sum(sof_values_3635.values()),
            'sum_data_3639': sum(sof_values_3639.values()),
            'sum_data_38105_sdit': sum(sof_values_38105_sdit.values()),
            'sum_data_38105_tkit_ae': sum(sof_values_38105_tkit_ae.values()),
            'sum_data_38105_tkit_ans': sum(sof_values_38105_tkit_ans.values()),
            'sum_if_per_date_3632': balance_date_3632,
            'sum_if_per_date_3633': balance_date_3633,
            'sum_if_per_date_3635': balance_date_3635,
            'sum_if_per_date_3639': balance_date_3639,
            'sum_if_per_date_38105': balance_date_38105,
            'gf_json_api_3632': gf_json_3632,
            'gf_json_api_dumps_3632': json.dumps(gf_json_3632),
            "user": request.user

            # 'userdata': json.dumps(userdata, indent=4)
        })
    else:
        demanded_access = "Komposisi Dana"
        return render(request, "dashboard/dist/401.html", {'userData': user, 'demand_access': demanded_access })
