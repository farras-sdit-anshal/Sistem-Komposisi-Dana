from django.shortcuts import render
from SistemInformasiKeuangan.forms.AdjusmentForms import AdjustmentForms
from SistemInformasiKeuangan.forms.ChoicesAdjustmentForms import ChoicesAdjustmentForms


def choose_adjustment(request):
    choice_form_adjustment = ChoicesAdjustmentForms()
    return render(request, "dashboard/dist/choice-adjustment.html", {"form": choice_form_adjustment, "user": request.user})


def adjustment(request):
    form_adjustment = AdjustmentForms()

    return render(request, "dashboard/dist/adjustment.html", {"form": form_adjustment, "user": request.user})
