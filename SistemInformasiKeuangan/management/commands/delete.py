import os
import csv
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from SistemInformasiKeuangan.models import SourceOfFunds


class Command(BaseCommand):
    help = "Untuk ettingup kumpulan dari sumber2 - sumber dana"

    def handle(self, *args, **options):

        self.stdout.write("Uncomment kode dibawah (Lihat pada Sistem Informasi Keuangan/management/commands/setupsof.py")
