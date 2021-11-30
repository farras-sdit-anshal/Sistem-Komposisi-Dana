import os
import csv
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from SistemInformasiKeuangan.models import VaType, SourceOfFunds


class Command(BaseCommand):
    help = "Untuk ettingup kumpulan dari sumber2 - sumber dana"

    def handle(self, *args, **options):

        self.stdout.write("Uncomment kode dibawah (Lihat pada Sistem Informasi Keuangan/management/commands/setupsof.py")
        # save_path = os.path.join(settings.MEDIA_ROOT, "va_type.csv")
        # numb = 0
        # with open(save_path) as csv_file:
        #     csv_reader = csv.DictReader(csv_file)
        #
        #     for data in csv_reader:
        #         # print(data)
        #         numb += 1
        #         # print(SourceOfFunds.objects.get(kode=data["Kode"]))
        #         VaType.objects.create(va_name=data["Keterangan"], va_id=data["VA"], code_id=SourceOfFunds.objects.get(kode = data["Kode"]).id)
        # self.stdout.write("Sumber dana berhasil di upload "+str(numb))
