from django.urls import path
from atlet.views import dash_atlet
from atlet.views import form_kualifikasi
from atlet.views import pertanyaan_kualifikasi
from atlet.views import daftar_atlet
from atlet.views import list_atlet
from atlet.views import register_sponsorship

app_name = 'atlet'

urlpatterns = [
    path('', dash_atlet, name='dash_atlet'),
    path('form_kualifikasi/', form_kualifikasi, name='form_kualifikasi'),
    path('form_kualifikasi/pertanyaan_kualifikasi/', pertanyaan_kualifikasi, name='pertanyaan_kualifikasi'),
    path('daftar_atlet/', daftar_atlet, name='daftar_atlet'),    
    path('daftar_atlet/list_atlet/', list_atlet, name='list_atlet'),
]