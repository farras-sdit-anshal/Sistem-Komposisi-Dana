from django.contrib import admin
from SistemInformasiKeuangan.models import *


# Setting interface dari tabel di admin model
class InterfaceAccount(admin.ModelAdmin):
    list_display = ('reference_number', "transaction_date",
                    "effective_date", "debit", "credit",
                    "balance", "description", "code_sof")


# Register your models here.
admin.site.register(SourceOfFunds)
admin.site.register(VaType)
admin.site.register(Account3639, InterfaceAccount)
admin.site.register(Account3635, InterfaceAccount)
admin.site.register(Account3632, InterfaceAccount)
admin.site.register(Account3633, InterfaceAccount)
admin.site.register(Account38105, InterfaceAccount)
admin.site.register(AccountAdjustment, InterfaceAccount)
