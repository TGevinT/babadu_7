from django.urls import path
from umpire.views import dash_umpire

app_name = 'umpire'

urlpatterns = [
    path('', dash_umpire, name='dash_umpire'),
    
]