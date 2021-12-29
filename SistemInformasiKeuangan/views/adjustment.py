from django.shortcuts import render
from SistemInformasiKeuangan.forms.AdjusmentForms import AdjustmentForms
from SistemInformasiKeuangan.forms.ChoicesAdjustmentForms import ChoicesAdjustmentForms
from SistemInformasiKeuangan.utils import validation


def choose_adjustment(request):
    user = request.user
    if validation.validation_groups(user, "Accountant"):
        choice_form_adjustment = ChoicesAdjustmentForms()
        return render(request, "dashboard/dist/choice-adjustment.html",
                      {"form": choice_form_adjustment, "user": user})
    else:
        demanded_access = "Input penyesuaian"
        return render(request, "dashboard/dist/401.html", {'userData': user, 'demand_access': demanded_access})


def adjustment(request):
    user = request.user
    if validation.validation_groups(user, "Accountant"):
        form_adjustment = AdjustmentForms()
        return render(request, "dashboard/dist/adjustment.html", {"form": form_adjustment, "user": user})
    else:
        demanded_access = "Input penyesuaian"
        return render(request, "dashboard/dist/401.html", {'userData': user, 'demand_access': demanded_access})
