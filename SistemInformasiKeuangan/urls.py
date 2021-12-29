from django.urls import path
import SistemInformasiKeuangan.views.views
import SistemInformasiKeuangan.views.adjustment

urlpatterns = [
    path('dashboard/', SistemInformasiKeuangan.views.views.dashboard),
    path('input-data/', SistemInformasiKeuangan.views.views.inputData),
    path('input-data/processing-data/', SistemInformasiKeuangan.views.views.processform),
    path('input-data/adjustment/', SistemInformasiKeuangan.views.adjustment.choose_adjustment),
    path('input-data/adjustment/exec', SistemInformasiKeuangan.views.adjustment.adjustment),
    path("", SistemInformasiKeuangan.views.views.index),
]
