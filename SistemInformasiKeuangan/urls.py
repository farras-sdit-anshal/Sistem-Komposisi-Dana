
from django.urls import path
import SistemInformasiKeuangan.views.views

urlpatterns = [
    path('dashboard/', SistemInformasiKeuangan.views.views.dashboard),
    path('input-data/', SistemInformasiKeuangan.views.views.inputData),
    path('input-data/processing-data/', SistemInformasiKeuangan.views.views.processform),
    path("", SistemInformasiKeuangan.views.views.index),
]
