import datetime
import json
import os
import mimetypes
import csv
import re
import xlrd
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from os.path import exists

# Create your views here.
from django.conf import settings


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
    return render(request, "dashboard/dist/input.html")


def processform(request):
    save_path = ""

    is_uploaded = request.FILES.get('file-mutasi', False)
    if is_uploaded:
        if request.method == 'POST':
            save_path = os.path.join(settings.MEDIA_ROOT, request.FILES["file-mutasi"].name)
            with open(save_path, "wb") as output_file:
                for chunk in request.FILES["file-mutasi"].chunks():
                    output_file.write(chunk)

        # cek apakah file tersebut exit
        if exists(save_path):
            for typeFile in mimetypes.guess_type(save_path):
                # print(mimetypes.guess_extension(typeFile))
                if typeFile is not None:
                    posible_extension = (mimetypes.guess_all_extensions(typeFile))
                    if ".csv" in posible_extension:
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

                                # Mengkalsifikasikan apakah transaksi tersebut virtual account atau tidak
                                is_va = re.search("VA : 8166", data['Keterangan'])
                                if is_va is not None:
                                    print(data)

        return render(request, "dashboard/dist/form-process.html")
    else:
        return redirect(inputData)


@login_required
def dashboard(request):
    user = request.user
    auth0user = user.social_auth.get(provider='auth0')
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture'],
        'email': auth0user.extra_data['email'],
    }

    return render(request, 'dashboard/dist/index.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4)
    })
