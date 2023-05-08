from django.urls import path
from pelatih.views import show_pelatih

app_name = 'pelatih'

urlpatterns = [
    path('', show_pelatih, name='show_pelatih'),
    
]