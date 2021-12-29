from django import forms
from SistemInformasiKeuangan.models import SourceOfFunds


class AdjustmentForms(forms.Form):
    # custome grid here has purpose to control grid width
    date_input0 = forms.DateField(label="Tanggal",
                                  widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control',
                                                                "placeholder": "Insert here", 'grid': 'col-2'}))

    SOF_CHOICES = SourceOfFunds.objects.all()

    # print(SOF_CHOICES)
    sof_input0 = forms.ModelChoiceField(queryset=SOF_CHOICES, label="Sumber Dana",
                                        widget=forms.Select(attrs={'class': 'form-control',
                                                                   "placeholder": "Insert here", 'grid': 'col-2'}))

    norefrensi_input0 = forms.CharField(label="Nomor Refrensi", widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                              "placeholder": "Insert here",
                                                                                              'grid': 'col-2'}))
    keterangan_input0 = forms.CharField(label="Keterangan", widget=forms.Textarea(attrs={'class': 'form-control',
                                                                                         "placeholder": "Insert here",
                                                                                         'grid': 'col-4'}))
    nominal_input0 = forms.IntegerField(label="Keterangan", widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                                            "placeholder": "Insert here",
                                                                                            'grid': 'col-2'}))
