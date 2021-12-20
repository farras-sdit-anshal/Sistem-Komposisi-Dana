from django.urls import path, include
import SistemInformasiKeuangan.views

urlpatterns = [
    path('dashboard/', SistemInformasiKeuangan.views.dashboard),
    path('input-data/', SistemInformasiKeuangan.views.inputData),
    path('input-data/processing-data/', SistemInformasiKeuangan.views.processform),
    path("", SistemInformasiKeuangan.views.index),
]
