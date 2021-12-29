from django import forms
from SistemInformasiKeuangan.models import *


class ChoicesAdjustmentForms(forms.Form):

    def __init__(self):
        super().__init__()

    date_input0 = forms.DateField(label="Tanggal",
                                  widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control',
                                                                "placeholder": "Insert here", 'grid': 'col-2'}))
