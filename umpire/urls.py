from django.urls import path
from umpire.views import dash_umpire
from umpire.views import show_pertandingan

app_name = 'umpire'

urlpatterns = [
    path('', dash_umpire, name='dash_umpire'),
     path('pertandingan/', show_pertandingan, name='pertandingan'),
    
]