from django.urls import path
from umpire.views import dash_umpire
from umpire.views import show_pertandingan
from umpire.views import show_semifinal
from umpire.views import show_final
from umpire.views import show_hasil
from umpire.views import show_hasil_pertandingan

app_name = 'umpire'

urlpatterns = [
    path('', dash_umpire, name='dash_umpire'),
    path('pertandingan/', show_pertandingan, name='pertandingan'),
    path('semifinal/', show_semifinal, name='semifinal'),
    path('final', show_final, name='final'),
    path('hasil', show_hasil, name='hasil'),
    path('hasil_pertandingan', show_hasil_pertandingan, name='hasil_pertandingan'),
    
]