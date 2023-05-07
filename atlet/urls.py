from django.urls import path
from atlet.views import dash_atlet

app_name = 'atlet'

urlpatterns = [
    path('', dash_atlet, name='dash_atlet'),
    
]