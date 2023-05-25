from django.urls import path
from atlet.views import dash_atlet
from atlet.views import form_kualifikasi
from atlet.views import pertanyaan_kualifikasi
from atlet.views import daftar_atlet
from atlet.views import list_atlet
from atlet.views import daftar_sponsor
from atlet.views import daftar_event
from atlet.views import daftar_event_lanjut
from atlet.views import daftar_partai
from atlet.views import enrolled_event



app_name = 'atlet'

urlpatterns = [
    path('', dash_atlet, name='dash_atlet'),
    path('form_kualifikasi/', form_kualifikasi, name='form_kualifikasi'),
    path('form_kualifikasi/pertanyaan_kualifikasi/', pertanyaan_kualifikasi, name='pertanyaan_kualifikasi'),
    path('daftar_atlet/', daftar_atlet, name='daftar_atlet'),    
    path('daftar_atlet/list_atlet/', list_atlet, name='list_atlet'),
    path('daftar_sponsor/', daftar_sponsor, name='daftar_sponsor'),
    path('daftar_event/', daftar_event, name='daftar_event'),
    path('daftar_event/daftar_event_lanjut/', daftar_event_lanjut, name='daftar_event_lanjut'),
    path('daftar_event/daftar_event_lanjut/pilih_kategori/', daftar_partai, name='pilih_kategori'),
    path('daftar_event/daftar_event_lanjut/pilih_kategori/enrolled_event/', enrolled_event, name='enrolled_event')
]